from marshmallow.validate import Validator
from marshmallow.exceptions import ValidationError
from src.models.Inventory import Inventory
from flask import request
import re

class ValueFormat(Validator):
    def __call__(self, value):
        #validate format
        regex = '\+\d{2}\s\d{2}\s\d{5}-\d{4}'
        pattern = re.compile(regex)
        if(not pattern.match(value)):
            raise ValidationError('The value must be format +00 00 00000-0000')
        return value