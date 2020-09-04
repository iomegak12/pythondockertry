from crmsystem.models import Order
from crmsystem.utilities import ErrorProvider

ERRORS = [
    {"errorKey": 1, "errorCode": "ORDENC101",
        "errorMessage": "Invalid Order Argument(s) Specified"}
]


class OrderEncoder:
    def transform(dictionary):
        if dictionary is None:
            raise ErrorProvider.get_error(1)

        order = Order(dictionary["orderId"], dictionary["orderDate"],
                      dictionary["customer"], dictionary["billingAddress"],
                      dictionary["amount"])

        return order
