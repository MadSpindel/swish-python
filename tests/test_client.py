import os
import unittest

import swish


class SwishClientTestCase(unittest.TestCase):
    def setUp(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        cert_file_path = os.path.join(current_folder, "cert.pem")
        key_file_path = os.path.join(current_folder, "key.pem")
        cert = (cert_file_path, key_file_path)
        self.client = swish.SwishClient(swish.Environment.Test, '1231181189', cert)

    def test_client(self):
        self.assertEqual(self.client.environment.base_url, swish.Environment.Test.base_url)
        self.assertEqual(self.client.payee_alias, '1231181189')

    def test_payment_request(self):
        response = self.client.payment_request(
            amount=1,
            currency='SEK',
            callback_url='https://fake-url.com/',
            payee_payment_reference='fake',
            message='fake'
        )
        print(response)
