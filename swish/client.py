import requests

from .environment import Environment
from .exceptions import SwishError
from .models import Payment, Refund

try:
    from requests.packages.urllib3.contrib import pyopenssl
    pyopenssl.extract_from_urllib3()
except ImportError:
    pass


class SwishClient(object):
    def __init__(self, environment, merchant_swish_number, cert, verify=False):
        self.environment = Environment.parse_environment(environment)
        self.merchant_swish_number = merchant_swish_number
        self.cert = cert
        self.verify = verify

    def __post(self, endpoint, payload):
        url = self.environment.base_url + endpoint
        return requests.post(url=url, json=payload.to_primitive(), headers={'Content-Type': 'application/json'},
                             cert=self.cert, verify=self.verify)

    def __get(self, endpoint, parameter):
        url = self.environment.base_url + endpoint + '/' + str(parameter)
        return requests.get(url, cert=self.cert, verify=self.verify)

    def create_payment(self, amount, currency, callback_url, payee_payment_reference=None, message=None,
                       payer_alias=None):
        payment_request = Payment({
            'payee_alias': self.merchant_swish_number,
            'amount': amount,
            'currency': currency,
            'callback_url': callback_url,
            'payee_payment_reference': payee_payment_reference,
            'message': message,
            'payer_alias': payer_alias
        })

        response = self.__post('paymentrequests', payment_request)
        if response.status_code == 422:
            raise SwishError(response.json())
        response.raise_for_status()

        return Payment({'id': response.headers.get('Location').split('/')[-1],
                        'location': response.headers.get('Location'),
                        'request_token': response.headers.get('PaymentRequestToken')})

    def get_payment(self, payment_request_id):
        response = self.__get('paymentrequests', payment_request_id)
        response.raise_for_status()
        return Payment(response.json())

    def create_refund(self, original_payment_reference, amount, currency, callback_url, payer_payment_reference=None,
                      payment_reference=None, payee_alias=None, message=None):
        refund_request = Refund({
            'payer_alias': self.merchant_swish_number,
            'payee_alias': payee_alias,
            'original_payment_reference': original_payment_reference,
            'amount': amount,
            'currency': currency,
            'callback_url': callback_url,
            'payer_payment_reference': payer_payment_reference,
            'payment_reference': payment_reference,
            'message': message
        })

        response = self.__post('refunds', refund_request)
        if response.status_code == 422:
            raise SwishError(response.json())
        response.raise_for_status()

        return Refund({'id': response.headers.get('Location').split('/')[-1],
                       'location': response.headers.get('Location')})

    def get_refund(self, refund_id):
        response = self.__get('refunds', refund_id)
        response.raise_for_status()
        return Refund(response.json())
