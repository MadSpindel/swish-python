import requests

from .environment import Environment
from .error import SwishError

try:
    from requests.packages.urllib3.contrib import pyopenssl
    pyopenssl.extract_from_urllib3()
except ImportError:
    pass


class SwishClient(object):
    def __init__(self, environment, payee_alias, cert, verify=False):
        self.environment = Environment.parse_environment(environment)
        self.payee_alias = payee_alias
        self.cert = cert
        self.verify = verify

    def post(self, endpoint, payload):
        url = self.environment.base_url + endpoint
        return requests.post(url=url, json=payload, headers={'Content-Type': 'application/json'}, cert=self.cert,
                             verify=self.verify)

    def get(self, url):
        return requests.get(url, cert=self.cert)

    def payment_request(self, amount, currency, callback_url, payee_payment_reference='', message='', payer_alias=''):
        payload = {
            'payeeAlias': self.payee_alias,
            'amount': amount,
            'currency': currency,
            'callbackUrl': callback_url,
            'payeePaymentReference': payee_payment_reference,
            'message': message,
        }
        if payer_alias:
            payload.update({'payer_alias': payer_alias})

        response = self.post('paymentrequests', payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise SwishError(response.json())
        return response

    def get_payment_request(self, payment_request_id):
        return self.get('paymentrequests/' + payment_request_id)

    def refund(self, amount, currency, callback_url, original_payment_reference, payer_payment_reference=''):
        payload = {
            'amount': amount,
            'currency': currency,
            'callback_url': callback_url
        }
        return self.post('refunds', payload)

    def get_refund(self, refund_id):
        return self.get('refunds/' + refund_id)
