# from src.tests.BaseTest import BaseTest
import unittest
from app import create_app

class TestSome(unittest.TestCase):
    app = None

    def setUp(self):
        self.app = create_app()

    def test_true(self):
        response = self.app.test_client().get('/api/v1/inventory/')
        self.assertEqual(response.status_code, 200)