# from src.tests.BaseTest import BaseTest
import unittest
from app import create_test_app
from src.models.Inventory import Inventory
from src.models import db
import time
import random

class TestSome(unittest.TestCase):
    app = None
    correct_data = {
        "value"         : "+55 86 90000-0002",
        "monthyPrice"   : 15,
        "currency"      : "R$",
        "setupPrice"    : 25,
    }
    update_data = {
        "value"         : "+55 86 90000-0003",
        "monthyPrice"   : 50,
        "currency"      : "U$",
        "setupPrice"    : 25,
    }
    incorrect_data = {
        "value"         : "86 90000000",
        "monthyPrice"   : -15,
        "currency"      : "",
        "setupPrice"    : -5,
    }
    instance = None

    def setUp(self):
        #create app
        self.app = create_test_app()
        #init with app test1
        db.init_app(self.app)
        #bind context
        self.app.app_context().push()
        #create instance for tests
        self.instance = Inventory(**{
            "value"         : "+55 86 90000-0000",
            "monthyPrice"   : 15,
            "currency"      : "R$",
            "setupPrice"    : 25,
        })
        self.instance.save()
    
    def tearDown(self):
        self.instance.delete()
    
    def generate_uri(self):
        return '/api/v1/inventory/' + str(self.instance.id)

    def test_can_list(self):
        response = self.app.test_client().get('/api/v1/inventory/')
        self.assertEqual(response.status_code, 200)
        res_decoed = response.get_json()
        self.assertTrue(res_decoed.get('result'))
    
    def test_can_create(self):
        response = self.app.test_client().post('/api/v1/inventory/', json=self.correct_data)
        self.assertEqual(response.status_code, 201)
        created_id = response.get_json().get('id')
        instance = Inventory.find(created_id)
        instance.delete()
    
    def test_can_edit(self):
        uri = self.generate_uri()
        response = self.app.test_client().put(uri, json=self.update_data)
        self.assertEqual(response.status_code, 200)

    def test_can_delete(self):
        uri = self.generate_uri()
        response = self.app.test_client().delete(uri)
        self.assertEqual(response.status_code, 204)