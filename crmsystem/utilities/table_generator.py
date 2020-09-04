from prettytable import PrettyTable
from crmsystem.utilities import ErrorProvider

ERRORS = [
    {"errorKey": 1, "errorCode": "CUSTTABGEN101",
        "errorMessage": "Invalid Customer(s) Specified"},
    {"errorKey": 2, "errorCode": "ORDTABGEN101",
        "errorMessage": "Invalid Order(s) Specified"},
]


class PrettyTableGenerator:
    def get_customer_table(customers):
        if customers is None:
            raise ErrorProvider.get_error(1)

        table = PrettyTable(["Id", "Name", "Address", "Credit", "Status"])

        for customer in customers:
            table.add_row([customer.id, customer.name,
                           customer.address, customer.credit, customer.status])

        return table

    def get_order_table(orders):
        if orders is None:
            raise ErrorProvider.get_error(2)

        table = PrettyTable(
            ["Order #", "Order Date", "Customer", "Address", "Amount"])

        for order in orders:
            table.add_row([order.orderId, order.orderDate,
                           order.customer, order.billingAddress, order.amount])

        return table
