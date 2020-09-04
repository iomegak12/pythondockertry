from flask import Flask, request, jsonify
from crmsystem.routing import CustomerRouteHandler

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/api/v1/customers", methods=["GET"])
def get_customers():
    customers = CustomerRouteHandler.get_customers()
    jsonify(customers)
