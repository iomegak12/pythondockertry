import unittest
import json
import requests
from crmsystem import CustomerEncoder


class GetCustomersTest(unittest.TestCase):
    """
    A class that helps to unit test complete functionalities of Customer service
    """
    def setUp(self):
        pass

    def test_successful_get_customers(self):
        """
        Test Customer Serivces Get Endpoint
        """
        response = requests.get('http://localhost:5000/api/v1/customers')

        responseText = response.text
        customers = json.loads(
            responseText, object_hook=CustomerEncoder.transform)
        
        actualNoOfCustomers = customers.__len__()
        expectedNoOfCustomers = 25

        assert actualNoOfCustomers == expectedNoOfCustomers
        assert response.status_code == 200

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
