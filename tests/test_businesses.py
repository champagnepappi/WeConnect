import unittest
import json
from app import create_app

class BusinessModelTestCase(unittest.TestCase):
    """This test case represents the business model testcase"""
    def setUp(self):
        """Initialize test variables"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.business = {"title": "Kenya wears", "location": "Nairobi",
        "description": "Some description here", "category": "Fashion"}

    def test_successful_business_creation(self):
        response =self.client.post('/api/v1/businesses', data=json.dumps(
        self.business), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_business_creation_with_blank_title(self):
        response = self.client.post('/api/v1/businesses',data=json.dumps(
        dict(title="", location="nakuru", description="lorem ipsum",
        category="Consultancy")), content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_should_return_all_the_businesses(self):
        response = self.client.get('/api/businesses')
        self.assertEqual(response.status, 200)

    def test_should_return_one_business(self):
        response = self.client.get('/api/businesses/1')
        self.assertEqual(response.status, 200)

    def test_should_delete_business(self):
        response = self.client.delete('/api/businesses/2')
        self.assertEqual(response.status, 200)

    def test_should_update_a_business(self):
        response = self.client.put('/api/businesses/3', data=json.dumps(
            dict(business_title="Johns hardware", description="This is just some hardware")),
            content_type="application/json" )
        self.assertEqual(response.status, 201)
