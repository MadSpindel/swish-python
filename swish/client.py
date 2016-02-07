from .environment import Environment


class SwishClient(object):
    def __init__(self, environment, payee_alias, cert):
        self.environment = Environment.parse_environment(environment)
        self.payee_alias = payee_alias
        self.cert = cert

    def post(self):
        print("Not implemented!")

    def payment_request(self, amount, currency, callback_url, payment_reference='', message=''):
        print("Not implemented!")

    def refund(self, amount, currency, callback_url):
        print("Not implemented!")
