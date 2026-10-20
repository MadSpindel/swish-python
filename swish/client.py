import uuid

import requests

from .environment import Environment
from .exceptions import SwishError
from .models import Payment, Refund, CommerceQRCodeRequest, Operation

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

        self.session = requests.Session()

    def __get(self, endpoint, parameter):
        url = self.environment.base_url + endpoint + '/' + str(parameter)
        return self.session.get( url    = url
                               , cert   = self.cert
                               , verify = self.verify
                               )

    def __post(self, endpoint, payload):
        if endpoint == 'commerce':
          base_url = self.environment.qr_url
        else:
          base_url = self.environment.base_url
        url = base_url + endpoint
        return self.session.post( url    = url
                                , json   = payload
                                , cert   = self.cert
                                , verify = self.verify)

    def __put(self, endpoint, payload):
        if endpoint == 'commerce':
          base_url = self.environment.qr_url
        else:
          base_url = self.environment.base_url
        url = base_url + endpoint
        return self.session.put( url    = url
                               , json   = payload
                               , cert   = self.cert
                               , verify = self.verify
                               )

    def __patch(self, endpoint, parameter, payload):
        url = self.environment.base_url + endpoint + '/' + str(parameter)
        return self.session.patch( url     = url
                                 , json    = payload
                                 , headers = {'Content-Type': 'application/json-patch+json'}
                                 , cert    = self.cert
                                 , verify  = self.verify
                                 )


    def create_payment( self
                      , amount
                      , currency
                      , callback_url
                      , callback_identifier     = None
                      , payee_payment_reference = None
                      , message                 = None
                      , payer_alias             = None
                      ):
        instruction_uuid = str(uuid.uuid4()).replace('-','').upper()
        payment_request = Payment({ 'payee_alias'             : self.merchant_swish_number
                                  , 'amount'                  : amount
                                  , 'currency'                : currency
                                  , 'callback_url'            : callback_url
                                  , 'callback_identifier'     : callback_identifier
                                  , 'payee_payment_reference' : payee_payment_reference
                                  , 'message'                 : message
                                  , 'payer_alias'             : payer_alias
                                  })

        response = self.__put(f'v2/paymentrequests/{instruction_uuid}', payment_request.to_primitive())
        if response.status_code == 422:
            raise SwishError(response.json())
        response.raise_for_status()

        return Payment({ 'id'            : response.headers.get('Location').split('/')[-1]
                       , 'location'      : response.headers.get('Location')
                       , 'request_token' : response.headers.get('PaymentRequestToken')
                       })

    def get_payment(self, payment_request_id):
        response = self.__get('v1/paymentrequests', payment_request_id)
        response.raise_for_status()
        return Payment(response.json())

    def cancel_payment(self, payment_request_id):
        operation = Operation()
        response = self.__patch('v1/paymentrequests', payment_request_id, [operation.to_primitive()])
        response.raise_for_status()
        return Payment(response.json())

    def create_refund( self
                     , original_payment_reference
                     , amount
                     , currency
                     , callback_url
                     , callback_identifier     = None
                     , payer_payment_reference = None
                     , payment_reference       = None
                     , payee_alias             = None
                     , message                 = None
                     ):
        instruction_uuid = str(uuid.uuid4()).replace('-','').upper()
        refund_request = Refund({ 'payer_alias': self.merchant_swish_number
                                , 'payee_alias': payee_alias
                                , 'original_payment_reference' : original_payment_reference
                                , 'amount'                     : amount
                                , 'currency'                   : currency
                                , 'callback_url'               : callback_url
                                , 'callback_identifier'        : callback_identifier
                                , 'payer_payment_reference'    : payer_payment_reference
                                , 'payment_reference'          : payment_reference
                                , 'message'                    : message
                                })

        response = self.__put(f'v2/refunds/{instruction_uuid}', refund_request.to_primitive())
        if response.status_code == 422:
            raise SwishError(response.json())
        response.raise_for_status()

        return Refund({ 'id'       : response.headers.get('Location').split('/')[-1]
                      , 'location' : response.headers.get('Location')
                      })

    def get_refund(self, refund_id):
        response = self.__get('v1/refunds', refund_id)
        response.raise_for_status()
        return Refund(response.json())


    def commerce_qr_code( self
                        , token
                        , format
                        , size        = None
                        , border      = None
                        , transparent = None
                        ):
        commerce_qr_code_request = CommerceQRCodeRequest({ 'token'       : token
                                                         , 'format'      : format
                                                         , 'size'        : size
                                                         , 'border'      : border
                                                         , 'transparent' : transparent
                                                         })

        response = self.__post('commerce', commerce_qr_code_request.to_primitive())
        response.raise_for_status()
        return response.content
