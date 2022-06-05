from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=256, null=True, blank=True)
    verification_code = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    street1 = models.CharField(max_length=256)
    street2 = models.CharField(max_length=256)
    state = models.CharField(max_length=3)
    city = models.CharField(max_length=20)
    zip = models.IntegerField()
    country = models.CharField(max_length=5, default='US')
    is_default = models.BooleanField(default=False)

class Shipment(models.Model):
    shipment_id = models.CharField(max_length=256)

    from_street1 = models.CharField(max_length=50)
    from_street2 = models.CharField(max_length=50, default=None)
    from_zip = models.IntegerField()
    from_phone = models.IntegerField()
    from_state = models.CharField(max_length=3)
    from_country = models.CharField(max_length=3, default='US')

    to_street1 = models.CharField(max_length=50)
    to_street2 = models.CharField(max_length=50, default=None)
    to_zip = models.IntegerField()
    to_phone = models.IntegerField()
    to_state = models.CharField(max_length=3)
    to_country = models.CharField(max_length=3, default='US')

    length = models.FloatField(default=1)
    height = models.FloatField(default=1)
    width = models.FloatField(default=1)
    weight = models.FloatField()

class Order_Status(models.Model):
    description = models.CharField(max_length=256)
    name = models.CharField(max_length=50)

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rate_id = models.CharField(max_length=225, null=True, blank=True)
    postage_label = models.CharField(max_length=225, null=True, blank=True)
    tracking_code = models.CharField(max_length=225, null=True, blank=True)
    carrer = models.CharField(max_length=20, null=True, blank=True)
    service = models.CharField(max_length=20, null=True, blank=True)
    status_id = models.ForeignKey(Order_Status, on_delete=models.CASCADE, null=True, blank=True)

class Order_Detail(models.Model):
    shipment_id = models.ManyToManyField(Shipment)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)