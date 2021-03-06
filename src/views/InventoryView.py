from flask import request, json, Response, Blueprint
from src.models.Inventory import Inventory
from src.serializers.InventorySerializer import inventory_serializer
from src.utils.response import bad_request, single_response, paginate, not_fount, no_content
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

@inventory_blueprint.route('/', methods=['GET'])
def index():
    """
    Return list of inventory entities
    """
    return paginate(Inventory, inventory_serializer)

@inventory_blueprint.route('/<inventory_id>', methods=['GET'])
def retrive(inventory_id):
    """
    Retrive one instance by id
    """
    instance = Inventory.find(inventory_id)
    if(instance):
        ser_instance = inventory_serializer.dump(instance)
        return single_response(ser_instance)
    return not_fount()

@inventory_blueprint.route('/<inventory_id>', methods=['PUT'])
def update(inventory_id):
    """
    Make update data of one instance
    """
    instance = Inventory.find(inventory_id)
    data_request = request.get_json()
    if(instance):
        #validate data from request
        try:
            inventory_serializer.context = {'id': inventory_id}
            data = inventory_serializer.load(data_request)
        except ValidationError as error:
            return bad_request(error)
        #make update of fields
        instance.update(data)
        ser_instance = inventory_serializer.dump(instance)
        return single_response(ser_instance)
    return not_fount()

@inventory_blueprint.route('/<inventory_id>', methods=['DELETE'])
def delete(inventory_id):
    """
    Remove one enttity from database
    """
    instance = Inventory.find(inventory_id)
    if(instance):
        instance.delete()
        return no_content()
    return not_fount()
