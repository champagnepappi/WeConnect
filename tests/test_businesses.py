import unittest
import os
import json
from app import create_app

class BusinessModelTestCase(unittest.TestCase):
    """This test case represents the business model testcase"""
    def setUp(self):
        """Initialize test variables"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_should_return_all_the_businesses(self):
        response = self.client().get('/api/businesses')
        self.assertEqual(response.status, 200)
