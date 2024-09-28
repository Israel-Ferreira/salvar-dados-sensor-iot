import json

from uuid import uuid4

# import requests

import boto3
from decimal import Decimal

import json


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("temperatures")

    event_dict =  event


    id =  uuid4()

    temperature_data = {
        "medicao_id": str(id),
        "temperatura": Decimal(str(event_dict["temperatura"])),
        "umidade_do_ar": Decimal(str(event_dict["umidade_do_ar"])),
        "device_id": event_dict["device_id"],
        "lat": Decimal(str(event_dict["lat"])),
        "long": Decimal(str(event_dict["lat"]))
    }


    table.put_item(Item=temperature_data)


    return {"message": "evento salvo no dynamodb"}



