import requests

from .environment import Environment


class SwishClient(object):
    def __init__(self, environment, payee_alias, cert):
        self.environment = Environment.parse_environment(environment)
        self.payee_alias = payee_alias
        self.cert = cert

    def post(self, endpoint, payload):
        url = self.environment.base_url + endpoint
        return requests.post(url=url, json=payload, headers={'Content-Type': 'application/json'}, cert=self.cert)

    def get(self, url):
        return requests.get(url, cert=self.cert)

    def payment_request(self, amount, currency, callback_url, payee_payment_reference='', message=''):
        payload = {
            'payeeAlias': self.payee_alias,
            'amount': amount,
            'currency': currency,
            'callbackUrl': callback_url,
            'payeePaymentReference': payee_payment_reference,
            'message': message
        }
        r = self.post('paymentrequests', payload)
        return r

    def get_payment_request(self, payment_request_id):
        r = self.get('paymentrequests/' + payment_request_id)
        return r

    def refund(self, amount, currency, callback_url, original_payment_reference, payer_payment_reference=''):
        payload = {
            'amount': amount,
            'currency': currency,
            'callback_url': callback_url
        }
        r = self.post('refunds', payload)
        return r

    def get_refund(self, refund_id):
        r = self.get('refunds/' + refund_id)
        return r
