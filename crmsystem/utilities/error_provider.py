from crmsystem.models import CRMSystemError


class ErrorProvider:
    def get_error(errors, errorKey):
        errorInfo = {}

        if errors and errorKey:
            for error in errors:
                if error["errorKey"] == errorKey:
                    errorInfo = error
                    break

        crmSystemError = CRMSystemError(
            errorInfo["errorCode"], errorInfo["errorMessage"])

        return crmSystemError
