import requests
import json
import threading

from crmsystem.models import Customer
from crmsystem.utilities import ErrorProvider, CustomerEncoder
from crmsystem.config import GlobalConfiguration

CUSTOMER_SERVICE_URL = "CUSTOMER_SERVICE_URL"

ERRORS = [
    {"errorId": 1, "errorKey": "CUSTSVC101",
        "errorMessage": "Invalid Customer Service Callback Specified"},
    {"errorId": 2, "errorKey": "CUSTSVC102",
        "errorMessage": "Invalid Customer Service URL Specified!"}
]


class CustomerService(threading.Thread):
    def __init__(self, callback):
        threading.Thread.__init__(self)

        if callback is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        self.callback = callback

        configuration = GlobalConfiguration.get_configuration()
        customerServiceUrl = configuration[CUSTOMER_SERVICE_URL]

        if customerServiceUrl is None:
            raise ErrorProvider.get_error(ERRORS, 2)

        self.customerServiceUrl = customerServiceUrl

    def run(self):
        response = requests.get(self.customerServiceUrl)
        responseText = response.text

        customers = json.loads(
            responseText, object_hook=CustomerEncoder.transform)

        if self.callback is not None:
            self.callback(customers)
