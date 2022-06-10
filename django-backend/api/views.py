from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from django.contrib.auth.models import User
from .serializer import CustomJWTSerializer, RegisterSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions


from .models import Customer, Order


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
        data = {"error": "error"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
