from flask import Flask, request, jsonify

from crmsystem.utilities import ErrorProvider
from crmsystem.services import CustomerService


class CustomerRouteHandler:
    @staticmethod
    def get_customers():
        customers = None

        def handle_results(customerRecords):
            customers = customerRecords

        customerService = CustomerService(handle_results)
        customerService.start()
        customerService.join()

        return customers
