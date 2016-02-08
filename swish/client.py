import json
import requests

from .environment import Environment


class SwishClient(object):
    def __init__(self, environment, payee_alias, cert):
        self.environment = Environment.parse_environment(environment)
        self.payee_alias = payee_alias
        self.cert = cert

    def post(self, endpoint, json):
        url = self.environment.base_url + endpoint
        r = requests.post(url=url, json=json, headers={'Content-Type': 'application/json'}, cert=self.cert)
        print(r)
        print("Not implemented!")

    def payment_request(self, amount, currency, callback_url, payment_reference='', message=''):
        data = {
            'amount': amount,
            'currency': currency,
            'callback_url': callback_url,
            'payment_reference': payment_reference,
            'message': message
        }
        print(json.dumps(data))
        print("Not implemented!")

    def refund(self, amount, currency, callback_url):
        data = {
            'amount': amount,
            'currency': currency,
            'callback_url': callback_url
        }
        print(json.dumps(data))
        print("Not implemented!")
