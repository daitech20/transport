from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from django.contrib.auth.models import User
from .serializer import CustomJWTSerializer, RegisterSerializer, OrderSerializer, UserSerializer, CustomerSerializer, ShipmentSerializer, CheckPriceShipmentSerializer, UpdateCheckPriceShipmentSerializer, SendMailSerializer, OrderCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .sendMail import sendMail



from .models import Customer, Order, Shipment, Parcel, CheckPriceShipment


# Create your views here.
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        print(serializer.data)
        order_id = serializer.data['id']

        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        exception = APIException(serializer.data)
        exception.status_code = status.HTTP_200_OK
        raise exception

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'order_id'

class CreateOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

class ValidateEmail(APIView):
    def get(self, request, email, code):
        customers = Customer.objects.all()
        for customer in customers:
            user = customer.user
            if user.email == email and customer.verification_code == "":
                data = {"result": "ok"}
                return Response(data, status=status.HTTP_200_OK)

            if user.email == email and customer.verification_code == code:
                customer.verification_code = ""
                customer.save()
                data = {"result": "ok"}
                return Response(data, status=status.HTTP_200_OK)
        data = {"error": "Email hoặc code không đúng"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer
    lookup_field = 'username'

class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all().select_related('user')
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CustomerSerializer
    lookup_field = 'username'

    def get_object(self):
        """Return the object for this view."""
        return get_object_or_404(self.queryset, user__username=self.kwargs["username"])

class ShipmentList(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShipmentDetail(generics.RetrieveAPIView):
    queryset = Shipment.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ShipmentSerializer

class CheckPriceShipmentList(generics.ListAPIView):
    queryset = CheckPriceShipment.objects.all()
    serializer_class = CheckPriceShipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CheckPriceShipmentDetail(generics.RetrieveAPIView):
    queryset = CheckPriceShipment.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CheckPriceShipmentSerializer
    lookup_field = 'shipment'

class UpdateCheckPriceShipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CheckPriceShipment.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UpdateCheckPriceShipmentSerializer
    lookup_field = 'shipment'

class SendMail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = SendMailSerializer
    lookup_field = 'username'

    def get(self, request, username):
        user = User.objects.get(username=username)
        customer = Customer.objects.get(user=user)
        email = user.email
        code = customer.verification_code
        sendMail(email, code)
        return self.retrieve(request, username)
