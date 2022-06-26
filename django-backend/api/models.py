from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=255, null=True, blank=True)
    verification_code = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def user__username(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255)
    state = models.CharField(max_length=3)
    city = models.CharField(max_length=20)
    zip = models.IntegerField()
    country = models.CharField(max_length=5, default='US')
    is_default = models.BooleanField(default=False)

class Parcel(models.Model):
    height = models.FloatField(default=10)
    length = models.FloatField(default=10)
    width = models.FloatField(default=10)
    weight = models.FloatField()
    postage_label = models.CharField(max_length=225, null=True, blank=True)
    tracking_code = models.CharField(max_length=225, null=True, blank=True)

class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    from_name = models.CharField(max_length=20)
    from_phone = models.CharField(max_length=10)
    from_street1 = models.CharField(max_length=50)
    from_state = models.CharField(max_length=3)
    from_city = models.CharField(max_length=20)
    from_country = models.CharField(max_length=10)
    from_zip = models.CharField(max_length=10)

    to_name = models.CharField(max_length=20)
    to_phone = models.CharField(max_length=10)
    to_street1 = models.CharField(max_length=50)
    to_state = models.CharField(max_length=3)
    to_city = models.CharField(max_length=20)
    to_country = models.CharField(max_length=10)
    to_zip = models.CharField(max_length=10)

    parcel = models.ManyToManyField(Parcel, related_name='shipments')

class ServiceCarrier(models.Model):
    carrier = models.CharField(max_length=20)
    service = models.CharField(max_length=255)
    rate = models.FloatField()

class CheckPriceShipment(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    servicecarrier = models.ManyToManyField(ServiceCarrier)

class OrderStatus(models.Model):
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=50)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    parcel = models.ManyToManyField(Parcel, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    price_user = models.FloatField(null=True, blank=True) # price of user
    price_admin = models.FloatField(null=True, blank=True) # price of service
    carrier = models.CharField(max_length=20, null=True, blank=True)
    service = models.CharField(max_length=20, null=True, blank=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=True, blank=True)