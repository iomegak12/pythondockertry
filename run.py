import json
from flask import Flask, request, jsonify
from crmsystem import CustomerService, CustomerEncoder

flaskApp = Flask(__name__)
flaskApp.config["DEBUG"] = True


@flaskApp.route("/api/v1/customers/", methods=["GET"])
def get_customers():
    customers = []

    def handle_results(customerRecords):
        for record in customerRecords:
            customers.append(record)

    customerService = CustomerService(handle_results)
    customerService.start()
    customerService.join()

    return json.dumps(
        customers, cls=CustomerEncoder)


flaskApp.run()
