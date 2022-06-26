import easypost
import json
from .models import Shipment
easypost.api_key = "EZAK510fe07cfeb04c8294849086d630f433tWaFTrrcCI9E0bKTctXfag"

def check_price_shipment(shipment_id):
    shipment = Shipment.objects.get(id=shipment_id)

    to_address = easypost.Address.create(
        verify=["delivery"],
        street1=shipment.from_street1,
        street2='',
        state=shipment.from_state,
        zip=shipment.from_zip,
        city=shipment.from_city,
        country=shipment.from_country,
        phone=shipment.from_phone,
        company=shipment.from_name
    )

    from_address = easypost.Address.create(
        verify=["delivery"],
        street1=shipment.to_street1,
        street2='',
        state=shipment.to_state,
        zip=shipment.to_zip,
        city=shipment.to_city,
        country=shipment.to_country,
        phone=shipment.to_phone,
        company=shipment.to_name
    )

    parcels = shipment.parcel.all()
    shipments = []

    for parcel in parcels:
        shipments.append({
            "parcel": {
                "height": parcel.height,
                "length": parcel.length,
                "width": parcel.width,
                "weight": parcel.weight
            }
        })

    print(shipments)

    order = easypost.Order.create(
        to_address=to_address,
        from_address=from_address,
        shipments=shipments
    )

    return order.rates