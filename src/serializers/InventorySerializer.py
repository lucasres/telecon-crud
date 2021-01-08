from marshmallow import fields, Schema, validates
from marshmallow.validate import Range
from src.models.Inventory import Inventory
from marshmallow.validate import ValidationError

class InventorySerializer(Schema):
    id = fields.Int()
    value = fields.Str(required=True)
    monthyPrice = fields.Float(
        required=True,
        validate=[
            Range(min=0)
        ]
    )
    setupPrice = fields.Float(
        required=True,
        validate=[
            Range(min=0)
        ]
    )
    currency = fields.Str(required=True)

    @validates('value')
    def validate_unique_value(self, value):
        exists = Inventory.query.filter_by(value=value).count()
        if(exists):
            raise ValidationError('The value is need unique')

inventory_serializer = InventorySerializer()