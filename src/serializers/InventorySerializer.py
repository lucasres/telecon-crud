from marshmallow import fields, Schema

class InventorySerializer(Schema):
    id = fields.Int()
    value = fields.Str(required=True)
    monthyPrice = fields.Float(required=True)
    setupPrice = fields.Float(required=True)
    currency = fields.Str(required=True)

inventory_serializer = InventorySerializer()