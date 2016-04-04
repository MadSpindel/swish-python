

class Payment(object):
    def __init__(self, id, request_token=None):
        self.id = id
        self.request_token = request_token
