from marshmallow import fields, Schema, validates
from marshmallow.validate import Range
from src.models.Inventory import Inventory
from marshmallow.validate import ValidationError

class InventorySerializer(Schema):
    id = fields.Int(dump_only=True)
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
        #base query
        qs = Inventory.query.filter(Inventory.value==value)
        #if pass id in context, exclude id from query
        if(self.context.get('id')):
            qs = qs.filter(Inventory.id != self.context['id'])
        if(qs.count()):
            raise ValidationError('The value is need unique')

inventory_serializer = InventorySerializer()