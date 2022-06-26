from django.urls import path, include
from .views import MyTokenObtainPairView, \
    RegisterView, ValidateEmail, OrderList,\
    OrderDetail, UserDetail, CustomerDetail,\
    ShipmentList, CheckPriceShipmentList,\
    CheckPriceShipmentDetail, UpdateCheckPriceShipmentDetail, ShipmentDetail, SendMail, CreateOrder
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user/<str:username>', UserDetail.as_view()),
    path('customer/<str:username>', CustomerDetail.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<str:order_id>', OrderDetail.as_view()),
    path('createorder/', CreateOrder.as_view()),
    path('shipment/', ShipmentList.as_view()),
    path('shipment/<int:pk>', ShipmentDetail.as_view()),
    path('checkpriceshipment/', CheckPriceShipmentList.as_view()),
    path('checkpriceshipment/<str:shipment>', CheckPriceShipmentDetail.as_view()),
    path('checkpriceshipment/update/<str:shipment>', UpdateCheckPriceShipmentDetail.as_view()),
    path('register/', RegisterView.as_view()),
    path('validateEmail/<str:email>/<str:code>', ValidateEmail.as_view(), name='validateEmail'),
    path('sendMail/<str:username>', SendMail.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]