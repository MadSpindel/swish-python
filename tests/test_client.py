import os
import unittest
from random import randint
import time

import swish


class SwishClientTestCase(unittest.TestCase):
    def setUp(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        cert_file_path = os.path.join(current_folder, "cert.pem")
        key_file_path = os.path.join(current_folder, "key.pem")
        cert = (cert_file_path, key_file_path)
        verify = os.path.join(current_folder, "swish.pem")
        self.client = swish.SwishClient(
            environment=swish.Environment.MSS,
            merchant_swish_number='1231181189',
            cert=cert,
            verify=verify
        )

    def test_client(self):
        self.assertEqual(self.client.environment.base_url, swish.Environment.MSS.base_url)
        self.assertEqual(self.client.merchant_swish_number, '1231181189')

    def test_create_payment_ecommerce(self):
        payer_alias = '467%i' % randint(1000000, 9999999)
        payment = self.client.create_payment(
            payee_payment_reference='0123456789',
            callback_url='https://example.com/api/swishcb/paymentrequests',
            payer_alias=payer_alias,
            amount=100,
            currency='SEK',
            message='Kingston USB Flash Drive 8 GB'
        )
        self.assertIsNotNone(payment.id)
        self.assertIsNotNone(payment.location)

    def test_create_payment_mcommerce(self):
        payment = self.client.create_payment(
            payee_payment_reference='0123456789',
            callback_url='https://example.com/api/swishcb/paymentrequests',
            amount=100,
            currency='SEK',
            message='Kingston USB Flash Drive 8 GB'
        )
        self.assertIsNotNone(payment.id)
        self.assertIsNotNone(payment.location)
        self.assertIsNotNone(payment.request_token)

    def test_create_payment_error(self):
        with self.assertRaises(swish.SwishError):
            self.client.create_payment(
                payee_payment_reference='0123456789',
                callback_url='https://example.com/api/swishcb/paymentrequests',
                amount=100,
                currency='SEK',
                message='BE18'
            )

    def test_get_payment(self):
        payment_request = self.client.create_payment(
            payee_payment_reference='0123456789',
            callback_url='https://example.com/api/swishcb/paymentrequests',
            amount=100,
            currency='SEK',
            message='Kingston USB Flash Drive 8 GB'
        )
        payment = self.client.get_payment(payment_request.id)
        self.assertEqual(payment.payee_payment_reference, '0123456789')
        self.assertEqual(payment.callback_url, 'https://example.com/api/swishcb/paymentrequests')
        self.assertEqual(payment.amount, 100)
        self.assertEqual(payment.currency, 'SEK')
        self.assertEqual(payment.message, 'Kingston USB Flash Drive 8 GB')

    def test_create_refund(self):
        payment_request = self.client.create_payment(
            payee_payment_reference='0123456789',
            callback_url='https://example.com/api/swishcb/paymentrequests',
            amount=100,
            currency='SEK',
            message='Kingston USB Flash Drive 8 GB'
        )
        time.sleep(5)
        payment = self.client.get_payment(payment_request.id)
        refund = self.client.create_refund(
            original_payment_reference=payment.payment_reference,
            amount=100,
            currency='SEK',
            callback_url='https://example.com/api/swishcb/refunds',
            payer_payment_reference='0123456789',
            message='Refund for Kingston USB Flash Drive 8 GB'
        )
        self.assertIsNotNone(refund.id)
        self.assertIsNotNone(refund.location)

    def test_get_refund(self):
        payment_request = self.client.create_payment(
            payee_payment_reference='0123456789',
            callback_url='https://example.com/api/swishcb/paymentrequests',
            amount=100,
            currency='SEK',
            message='Kingston USB Flash Drive 8 GB'
        )
        time.sleep(5)
        payment = self.client.get_payment(payment_request.id)
        refund_request = self.client.create_refund(
            original_payment_reference=payment.payment_reference,
            amount=100,
            currency='SEK',
            callback_url='https://example.com/api/swishcb/refunds',
            payer_payment_reference='0123456789',
            message='Refund for Kingston USB Flash Drive 8 GB'
        )
        refund = self.client.get_refund(refund_request.id)
        self.assertEqual(refund.original_payment_reference, payment.payment_reference)
        self.assertEqual(refund.callback_url, 'https://example.com/api/swishcb/refunds')
        self.assertEqual(refund.amount, 100)
        self.assertEqual(refund.currency, 'SEK')
        self.assertEqual(refund.message, 'Refund for Kingston USB Flash Drive 8 GB')
