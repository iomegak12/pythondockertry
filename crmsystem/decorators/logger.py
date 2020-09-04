from datetime import datetime


class Logger(object):
    def __init__(self, pre: bool = True, post: bool = True):
        super().__init__()
        self.pre = pre
        self.post = post

    def __call__(self, function):
        def wrap_call(*args, **kargs):
            if self.pre:
                startTime = datetime.now()
                print('{} Log Started ...'.format(startTime))

            function(*args, **kargs)

            if self.post:
                endTime = datetime.now()
                print('{} Log Ended ...'.format(endTime))

        return wrap_call
