from crmsystem.decorators import Logger
from injector import inject
from crmsystem.services import CustomerService, OrderService
from crmsystem.utilities import ErrorProvider

ERRORS = [
    {"errorId": 1, "errorKey": "DATCONT101",
        "errorMessage": "Invalid Controller Callback Specified!"},
    {"errorId": 2, "errorKey": "DATCONT102",
        "errorMessage": "Invalid Customer Service Specified!"},
    {"errorId": 3, "errorKey": "DATCONT103",
        "errorMessage": "Invalid Order Service Specified!"},

]


class DataController:
    @inject
    def __init__(self, customerService: CustomerService, orderService: OrderService):
        if customerService is None:
            raise ErrorProvider.get_error(ERRORS, 2)

        self.customerService = customerService

        if orderService is None:
            raise ErrorProvider.get_error(ERRORS, 3)

        self.orderService = orderService

    @Logger(pre=True, post=True)
    def process(self, callback):
        if callback is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        self.customerService.start()
        self.orderService.start()

        self.customerService.join()
        self.orderService.join()

        callback()
