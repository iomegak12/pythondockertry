# import unittest
# import json
# from crmsystem import flaskApp, CustomerEncoder


# class GetCustomersTest(unittest.TestCase):
#     def setUp(self):
#         self.app = flaskApp.test_client()

#     def test_successful_get_customers(self):
#         response = self.app.get("/api/v1/customers/",
#                                 headers={"Content-Type": "application/json"})

#         expectedNoOfCustomers = 25
#         customers = json.loads(
#             response.json, object_hook=CustomerEncoder.transform)
#         actualNoOfCustomers = customers.__len__()

#         self.assertEqual(expectedNoOfCustomers, actualNoOfCustomers)
#         self.assertEqual(200, response.status_code)

#     def tearDown(self):
#         return super().tearDown()


# if __name__ == "__main__":
#     unittest.main()
