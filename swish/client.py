

class SwishClient(object):
    def __init__(self, payee_alias, cert):
        self.payee_alias = payee_alias
        self.cert = cert

    def payment_request(self, amount, currency, callback_url, payment_reference='', message=''):
        print("Not implemented!")

    def refund(self, amount, currency, callback_url):
        print("Not implemented!")
