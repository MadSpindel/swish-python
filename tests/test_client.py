import unittest

from swish.client import SwishClient


class SwishClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = SwishClient('fake-alias', 'fake-cert')

    def test_payment_request(self):
        self.fail("Not implemented!")

    def test_refund(self):
        self.fail("Not implemented!")
