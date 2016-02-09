import responses
import unittest

import swish

LOCATION = 'https://swicpc.bankgirot.se/swishcpcapi/api/v1/paymentrequests/AB23D7406ECE4542A80152D909EF9F6B'


class SwishClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = swish.SwishClient(swish.Environment.Test, 'fake-alias', 'fake-cert')

    def test_client(self):
        self.assertEqual(self.client.environment.base_url, swish.Environment.Test.base_url)
        self.assertEqual(self.client.payee_alias, 'fake-alias')
        self.assertEqual(self.client.cert, 'fake-cert')

    @responses.activate
    def test_payment_request(self):
        def request_callback(request):
            headers = {
                'Location': LOCATION
            }
            return (201, headers)

        responses.add_callback(
            responses.POST,
            self.client.environment.base_url + 'paymentrequests',
            callback=request_callback,
            content_type='application/json'
        )

        self.client.payment_request(
            amount=1, currency='SEK', callback_url='https://fake-url.com/', payment_reference='fake', message='fake'
        )
        self.fail("Not implemented!")

    @responses.activate
    def test_refund(self):
        self.fail("Not implemented!")
