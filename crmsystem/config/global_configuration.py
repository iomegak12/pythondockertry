import os
from crmsystem.models import CRMSystemError
from crmsystem.utilities import ErrorProvider

CUSTOMER_SERVICE_URL = "CUSTOMER_SERVICE_URL"
MONGO_SERVER = "MONGO_SERVER"
MONGO_PORT = "MONGO_PORT"
MONGO_DB = "MONGO_DB"

ERRORS = [
    {"errorKey": 1, "errorCode": "CONFERR101",
        "errorMessage": "Invalid Customer URL Specified"},
    {"errorKey": 2, "errorCode": "CONFERR102",
        "errorMessage": "Invalid Mongo Server Specified"},
    {"errorKey": 3, "errorCode": "CONFERR103",
        "errorMessage": "Invalid Mongo Port Specified"},
    {"errorKey": 4, "errorCode": "CONFERR104",
        "errorMessage": "Invalid Mongo Database Specified"},
]


class GlobalConfiguration:
    configuration = {}

    def get_configuration():
        isConfigurationNull = GlobalConfiguration.configuration is not None
        configurationLength = GlobalConfiguration.configuration.__len__()

        if isConfigurationNull and configurationLength > 0:
            return GlobalConfiguration.configuration

        customerServiceUrl = os.environ.get(CUSTOMER_SERVICE_URL, None)

        if customerServiceUrl is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        mongoServer = os.environ.get(MONGO_SERVER, None)

        if mongoServer is None:
            raise ErrorProvider.get_error(ERRORS, 2)

        mongoPort = os.environ.get(MONGO_PORT, None)

        if mongoPort is None:
            raise ErrorProvider.get_error(ERRORS, 3)

        mongoDB = os.environ.get(MONGO_DB, None)

        if mongoDB is None:
            raise ErrorProvider.get_error(ERRORS, 4)

        GlobalConfiguration.configuration[CUSTOMER_SERVICE_URL] = customerServiceUrl
        GlobalConfiguration.configuration[MONGO_SERVER] = mongoServer
        GlobalConfiguration.configuration[MONGO_PORT] = mongoPort
        GlobalConfiguration.configuration[MONGO_DB] = mongoDB

        return GlobalConfiguration.configuration
