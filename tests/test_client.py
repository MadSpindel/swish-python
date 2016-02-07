import unittest

import swish


class SwishClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = swish.SwishClient(swish.Environment.Test, 'fake-alias', 'fake-cert')

    def test_client(self):
        self.assertEqual(self.client.environment.base_url, swish.Environment.Test.base_url)
        self.assertEqual(self.client.payee_alias, 'fake-alias')
        self.assertEqual(self.client.cert, 'fake-cert')

    def test_payment_request(self):
        self.fail("Not implemented!")

    def test_refund(self):
        self.fail("Not implemented!")
