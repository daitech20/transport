from django.contrib import admin
from .models import Customer, Address, Shipment, Order, Order_Detail, Order_Status
# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Shipment)
admin.site.register(Order)
admin.site.register(Order_Detail)
admin.site.register(Order_Status)