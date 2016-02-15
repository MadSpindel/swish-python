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
        return requests.post(url=url, json=json, headers={'Content-Type': 'application/json'}, cert=self.cert)

    def get(self, endpoint, id):
        print("Not implemented yet!")

    def payment_request(self, amount, currency, callback_url, payee_payment_reference='', message=''):
        data = {
            'payeeAlias': self.payee_alias,
            'amount': amount,
            'currency': currency,
            'callbackUrl': callback_url,
            'payeePaymentReference': payee_payment_reference,
            'message': message
        }
        r = self.post('paymentrequests', json.dumps(data))
        return r

    def get_payment_request(payment_request_id):
        print("Not implemented yet!")

    def refund(self, amount, currency, callback_url, original_payment_reference, payer_payment_reference=''):
        data = {
            'amount': amount,
            'currency': currency,
            'callback_url': callback_url
        }
        r = self.post('refunds', json.dumps(data))
        return r

    def get_refund(refund_id):
        print("Not implemented yet!")
