from django.urls import path, include
from .views import MyTokenObtainPairView, RegisterView, ValidateEmail, OrderList, OrderDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('order/', OrderList.as_view()),
    path('order/<str:order_id>', OrderDetail.as_view()),
    path('register/', RegisterView.as_view()),
    path('validateEmail/<str:email>/<str:code>/', ValidateEmail.as_view(), name='validateEmail'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]