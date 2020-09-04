class CRMSystemError(Exception):
    def __init__(self, errorCode, errorMessage, *args, **kwargs):
        super().__init__(errorMessage, *args, **kwargs)
        self.errorCode = errorCode
        self.errorMessage = errorMessage

    def __str__(self):
        return "{} - {}".format(self.errorCode, self.errorMessage)
