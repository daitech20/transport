from django.contrib import admin
from .models import Customer, Address, Shipment, Parcel, ServiceCarrier, CheckPriceShipment
# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Shipment)
admin.site.register(Parcel)
admin.site.register(ServiceCarrier)
admin.site.register(CheckPriceShipment)