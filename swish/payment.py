

class Payment(object):
    def __init__(self, location, request_token=None):
        self.id = location.split('/')[-1]
        self.location = location
        self.request_token = request_token
