import threading

from pymongo import MongoClient
from crmsystem.models import Order
from crmsystem.utilities import OrderEncoder, ErrorProvider
from crmsystem.config import GlobalConfiguration

MONGO_SERVER = "MONGO_SERVER"
MONGO_PORT = "MONGO_PORT"
MONGO_DB = "MONGO_DB"
ORDERS_COLLECTION = "orders"

ERRORS = [
    {"errorId": 1, "errorCode": "ORDSVC101",
        "errorMessage": "Invalid Mongo Server Specified!"},
    {"errorId": 2, "errorCode": "ORDSVC102",
        "errorMessage": "Invalid Mongo Port Specified!"},
    {"errorId": 3, "errorCode": "ORDSVC103",
        "errorMessage": "Invalid Mongo DB Specified!"},
    {"errorId": 4, "errorCode": "ORDSVC104",
        "errorMessage": "Invalid Orders Callback Specified!"}
]


class OrderService (threading.Thread):
    def __init__(self, callback):
        threading.Thread.__init__(self)

        if callback is None:
            raise ErrorProvider.get_error(ERRORS, 4)

        self.callback = callback

        configuration = GlobalConfiguration.get_configuration()
        mongoServer = configuration[MONGO_SERVER]

        if mongoServer is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        mongoPort = configuration[MONGO_PORT]

        if mongoPort is None:
            raise ErrorProvider.get_error(ERRORS, 2)

        mongoDB = configuration[MONGO_DB]

        if mongoDB is None:
            raise ErrorProvider.get_error(ERRORS, 3)

        self.mongoServer = mongoServer
        self.mongoPort = mongoPort
        self.mongoDB = mongoDB

    def run(self):
        client = MongoClient(host=self.mongoServer, port=int(self.mongoPort))
        db = client[self.mongoDB]
        collection = db[ORDERS_COLLECTION]
        orders = collection.find({})

        internetOrders = []

        for order in orders:
            internetOrders.append(
                OrderEncoder.transform(order))

        if self.callback:
            self.callback(internetOrders)
