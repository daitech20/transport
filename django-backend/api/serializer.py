import easypost
easypost.api_key = "EZAK510fe07cfeb04c8294849086d630f433tWaFTrrcCI9E0bKTctXfag"
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from django.contrib.auth.models import User
from .models import Customer, Order, Shipment, Parcel, CheckPriceShipment, ServiceCarrier
from rest_framework.response import Response
from rest_framework import status
from .check_price_shipment import check_price_shipment
from .get_place_by_zipcode import get_place
from .sendMail import sendMail
import string
import random

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Order
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"error": "Password fields didn't match"})
        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=attrs['password'])
            # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['error'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return attrs


    def create(self, validated_data):
        if User.objects.filter(username=validated_data["username"]).exists():
            raise serializers.ValidationError({"username": "username exits"})
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError({"email": "email exists"})
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        chars_fixed = string.ascii_letters + string.digits
        min_size_pass = 8
        max_size_pass = 15
        password = "".join(random.choice(chars_fixed) for x in range(random.randint(min_size_pass, max_size_pass)))

        customer = Customer.objects.create (
            user = user,
            verification_code = password
        )

        customer.save()
        try:
            sendMail(user.email, customer.verification_code)
        except:
            print("send mail error")

        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include

        data.update({'id': self.user.id})
        data.update({'user': self.user.username})
        data.update({'email': self.user.email})
        data.update({'first_name': self.user.first_name})
        data.update({'last_name': self.user.last_name})
        data.update({'is_superuser': self.user.is_superuser})

        try:
            customer = Customer.objects.get(user=self.user)
            print("ok")
            data.update({'avatar': customer.avatar})
            data.update({'verification_code': customer.verification_code})
            data.update({'is_customer': True})

        except:
            data.update({'is_customer': False})

        # and everything else you want to send in the response
        return data

class CustomJWTSerializer(MyTokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }
        # This is answering the original question, but do whatever you need here.
        # For example in my case I had to check a different model that stores more user info
        # But in the end, you should obtain the username to continue.
        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'username', 'first_name', 'last_name', 'email']
        lookup_field = 'username'

class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Customer
        lookup_field = "username"
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    parcel = ParcelSerializer(many=True)

    class Meta:
        model = Shipment
        fields = '__all__'
        extra_kwargs = {
            'from_city': {'required': False},
            'from_name': {'required': False},
            'from_state': {'required': False},
            'to_city': {'required': False},
            'to_name': {'required': False},
            'to_state': {'required': False}
        }

    def validate(self, attrs):

        from_zip = get_place(attrs['from_zip'])
        to_zip = get_place(attrs['to_zip'])

        print(from_zip)
        print(to_zip)

        errors = dict()
        try:
            # validate the password and catch the exception
            if (from_zip['error']):
                errors['from_error'] = "Sai zipcpode"

            # the exception raised here is different than serializers.ValidationError
        except:
            attrs['from_city'] = from_zip['city']
            attrs['from_state'] = from_zip['state']
            attrs['from_name'] = 'abc'

        try:
            # validate the password and catch the exception
            if (to_zip['error']):
                errors['to_error'] = "Sai zipcode"
            # the exception raised here is different than serializers.ValidationError
        except:
            attrs['to_city'] = to_zip['city']
            attrs['to_state'] = to_zip['state']
            attrs['to_name'] = 'xyz'

        if errors:
            raise serializers.ValidationError(errors)

        return attrs


    def create(self, validated_data):
        # get the value from the payload.
        parcels = validated_data.pop('parcel')

        # Add (all) the value from payload to the Profile model.
        shipment_instance = Shipment.objects.create(**validated_data)

        # Loop the values that were passed inside of property fields from payload.
        for parcel in parcels:
            # Add normally the fields of "this payload" to the Property model.
            parcel_instance = Parcel.objects.create(**parcel)

            # Here is where the magic begins:
            # Get the property_instance and passes all the payloads.id.
            # and add them to profile_instance as it should be.
            shipment_instance.parcel.add(parcel_instance.id)

            # save the values.
            shipment_instance.save()

        rates = check_price_shipment(shipment_instance.id)

        shipment = CheckPriceShipment.objects.create(shipment_id = shipment_instance.id)

        for rate in rates:
            service_carrier = ServiceCarrier.objects.create(
                rate=rate.rate,
                carrier=rate.carrier,
                service=rate.service
            )
            shipment.servicecarrier.add(service_carrier)
            shipment.save()

        print(shipment)

        return shipment_instance

class ServiceCarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCarrier
        fields = '__all__'

class CheckPriceShipmentSerializer(serializers.ModelSerializer):
    servicecarrier = ServiceCarrierSerializer(many=True)
    class Meta:
        model = CheckPriceShipment
        fields = '__all__'
        extra_kwargs = {
            'servicecarrier': {'required': False}
        }

class UpdateCheckPriceShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckPriceShipment
        fields = '__all__'
        extra_kwargs = {
            'servicecarrier': {'required': False}
        }

class SendMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        lookup_field = 'username'

class OrderCreateSerializer(serializers.ModelSerializer):
    parcel = ParcelSerializer(many=True)

    from_name = serializers.CharField(write_only=True, max_length=20)
    from_phone = serializers.CharField(write_only=True, max_length=10)
    from_street1 = serializers.CharField(write_only=True, max_length=50)
    from_state = serializers.CharField(write_only=True, max_length=3)
    from_city = serializers.CharField(write_only=True, max_length=20)
    from_country = serializers.CharField(write_only=True, max_length=10)
    from_zip = serializers.CharField(write_only=True, max_length=10)
    from_company = serializers.CharField(write_only=True, max_length=20)

    to_name = serializers.CharField(write_only=True, max_length=20)
    to_phone = serializers.CharField(write_only=True, max_length=10)
    to_street1 = serializers.CharField(write_only=True, max_length=50)
    to_state = serializers.CharField(write_only=True, max_length=3)
    to_city = serializers.CharField(write_only=True, max_length=20)
    to_country = serializers.CharField(write_only=True, max_length=10)
    to_zip = serializers.CharField(write_only=True, max_length=10)
    to_company = serializers.CharField(write_only=True, max_length=20)
    rate = serializers.FloatField(write_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        # get the value from the payload.
        parcels = validated_data.pop('parcel')

        # Add (all) the value from payload to the Profile model.
        order_instance = Order.objects.create(user = validated_data.pop('user'))

        from_name = validated_data.pop('from_name')
        from_phone = validated_data.pop('from_phone')
        from_street1 = validated_data.pop('from_street1')
        from_state = validated_data.pop('from_state')
        from_city = validated_data.pop('from_city')
        from_country = validated_data.pop('from_country')
        from_zip = validated_data.pop('from_zip')
        from_company = validated_data.pop('from_company')

        to_name = validated_data.pop('to_name')
        to_phone = validated_data.pop('to_phone')
        to_street1 = validated_data.pop('to_street1')
        to_state = validated_data.pop('to_state')
        to_city = validated_data.pop('to_city')
        to_country = validated_data.pop('to_country')
        to_zip = validated_data.pop('to_zip')
        to_company = validated_data.pop('to_company')

        carrier = validated_data.pop('carrier')
        service = validated_data.pop('service')
        rate = validated_data.pop('rate')

        from_address = easypost.Address.create(
            verify=["delivery"],
            street1=from_street1,
            street2='',
            state=from_state,
            zip=from_zip,
            city=from_city,
            country=from_country,
            phone=from_phone,
            company=from_company if from_company != '' else from_name,
            name=from_name
        )

        to_address = easypost.Address.create(
            verify=["delivery"],
            street1=to_street1,
            street2='',
            state=to_state,
            zip=to_zip,
            city=to_city,
            country=to_country,
            phone=to_phone,
            company=to_company if to_company != '' else to_name,
            name=to_name
        )

        shipments = []
        for parcel in parcels:
            shipments.append({
                "parcel": {
                    "weight": parcel['weight'],
                    "length": parcel['length'],
                    "width": parcel['width'],
                    "height": parcel['height']
                }
            })
        errors = dict()
        try:
            order = easypost.Order.create(
                to_address=to_address,
                from_address=from_address,
                shipments=shipments
            )
        except easypost.Error as e:
            errors = e.json_body["error"]
            order_instance.delete()

        try:
            order.buy(carrier=carrier, service=service)
        except easypost.Error as e:
            errors = e.json_body["error"]
            order_instance.delete()

        if errors:
            raise serializers.ValidationError(errors)

        order_instance.carrier = carrier
        order_instance.service = service
        order_instance.price_user = rate
        order_instance.price_admin = order['shipments'][0]['selected_rate']['rate']
        order_instance.order_id = order.id

        # Loop the values that were passed inside of property fields from payload.
        temp = 0
        for parcel in parcels:
            # Add normally the fields of "this payload" to the Property model.
            parcel_instance = Parcel.objects.create(**parcel)
            parcel_instance.tracking_code = order['shipments'][temp]['tracking_code']
            parcel_instance.postage_label = order['shipments'][temp]['postage_label']['label_url']
            parcel_instance.save()
            # Here is where the magic begins:
            # Get the property_instance and passes all the payloads.id.
            # and add them to profile_instance as it should be.
            order_instance.parcel.add(parcel_instance.id)

            # save the values.
            order_instance.save()
            temp += 1

        shipments = Shipment.objects.all()
        for shipment in shipments:
            parcels = shipment.parcel.all()
            for parcel in parcels:
                parcel.delete()
            shipment.delete()

        price_shipments = CheckPriceShipment.objects.all()
        for price_shipment in price_shipments:
            servicecarriers = price_shipment.servicecarrier.all()
            for servicecarrier in servicecarriers:
                servicecarrier.delete()
            price_shipment.delete()

        return order_instance