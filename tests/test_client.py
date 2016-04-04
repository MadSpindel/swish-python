import os
import unittest

import swish


class SwishClientTestCase(unittest.TestCase):
    def setUp(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        cert_file_path = os.path.join(current_folder, "cert.pem")
        key_file_path = os.path.join(current_folder, "key.pem")
        cert = (cert_file_path, key_file_path)
        verify = os.path.join(current_folder, "swish.pem")
        self.client = swish.SwishClient(
            environment=swish.Environment.Test,
            payee_alias='1231181189',
            cert=cert,
            verify=verify
        )

    def test_client(self):
        self.assertEqual(self.client.environment.base_url, swish.Environment.Test.base_url)
        self.assertEqual(self.client.payee_alias, '1231181189')

    def test_payment_request_ecommerce(self):
        payment = self.client.payment_request(
            payee_payment_reference='0123456789',
            callback_url='https://example.com/api/swishcb/paymentrequests',
            payer_alias='4671234768',
            amount=100,
            currency='SEK',
            message='Kingston USB Flash Drive 8 GB'
        )
        self.assertIsNotNone(payment.id)

    def test_payment_request_mcommerce(self):
        payment = self.client.payment_request(
            payee_payment_reference='0123456789',
            callback_url='https://example.com/api/swishcb/paymentrequests',
            amount=100,
            currency='SEK',
            message='Kingston USB Flash Drive 8 GB'
        )
        self.assertIsNotNone(payment.id)
        self.assertIsNotNone(payment.request_token)

    def test_payment_request_error(self):
        with self.assertRaises(swish.SwishError):
            self.client.payment_request(
                payee_payment_reference='0123456789',
                callback_url='https://example.com/api/swishcb/paymentrequests',
                amount=100,
                currency='SEK',
                message='BE18'
            )
