import json
from crmsystem.models import Customer
from crmsystem.utilities import ErrorProvider

ERRORS = [
    {"errorKey": 1, "errorCode": "CUSTENC101",
        "errorMessage": "Invalid Customer Argument(s) Specified"}
]


class CustomerEncoder(json.JSONEncoder):
    @staticmethod
    def transform(dictionary):
        if dictionary is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        customer = Customer(dictionary["id"], dictionary["name"],
                            dictionary["address"], dictionary["credit"], dictionary["status"],
                            dictionary["remarks"])

        return customer

    def default(self, o):
        return o.__dict__
