import json


class Customer:
    def __init__(self, id, name, address, credit, status, remarks):
        super().__init__()
        self.id = id
        self.name = name
        self.address = address
        self.credit = credit
        self.status = status
        self.remarks = remarks

    def __str__(self):
        message = "{}, {}, {}, {}, {}, {}".format(
            self.id, self.name, self.address, self.credit, self.status, self.remarks)

        return message

    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()
