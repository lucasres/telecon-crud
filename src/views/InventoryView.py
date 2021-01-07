from flask import request, json, Response, Blueprint
from src.models.Inventory import Inventory
from src.serializers.InventorySerializer import inventory_serializer
from src.utils.response import bad_request, single_response
from marshmallow.exceptions import ValidationError

inventory_blueprint = Blueprint('inventory', __name__)

@inventory_blueprint.route('/', methods=['POST'])
def create():
    """
    Create new inventory entity
    """
    data_request = request.get_json()
    #parse data from request
    try:
        data = inventory_serializer.load(data_request)
    except ValidationError as error:
        return bad_request(error)
    #handle create instance and save
    instance = Inventory(**data)
    instance.save()
    #serialize response
    res_instance = inventory_serializer.dump(instance)
    return single_response(res_instance, 201)