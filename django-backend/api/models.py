from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=256, null=True, blank=True)
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
    street1 = models.CharField(max_length=256)
    street2 = models.CharField(max_length=256)
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

class OrderStatus(models.Model):
    description = models.CharField(max_length=256)
    name = models.CharField(max_length=50)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=256, unique=True)
    shipment_id = models.CharField(max_length=256, unique=True)
    parcel = models.ManyToManyField(Parcel, null=True, blank=True)
    rate_id = models.CharField(max_length=225, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    price_user = models.FloatField(null=True, blank=True) # price of user
    price_admin = models.FloatField(null=True, blank=True) # price of service
    postage_label = models.CharField(max_length=225, null=True, blank=True)
    tracking_code = models.CharField(max_length=225, null=True, blank=True)
    carrier = models.CharField(max_length=20, null=True, blank=True)
    service = models.CharField(max_length=20, null=True, blank=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=True, blank=True)