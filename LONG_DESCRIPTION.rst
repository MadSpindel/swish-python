Swish Python Client Library
===========================

This client library is designed to support the Swish API.

Installation
------------

It's easy! Just install it with pip:

.. code-block:: bash

    $ pip install swish

Quick Start Example
-------------------

.. code-block:: python

    import swish
    
    swish_client = swish.SwishClient(
        environment=swish.Environment.MSS,
        merchant_swish_number='1231181189',
        cert=('/path/to/cert.pem', '/path/to/key.pem'),
        verify='/path/to/swish.pem'
    )
    
    payment = swish_client.create_payment(
        payee_payment_reference='0123456789',
        callback_url='https://example.com/api/swishcb/paymentrequests',
        payer_alias='46712345678',
        amount=100,
        currency='SEK',
        message='Kingston USB Flash Drive 8 GB'
    )
    
    # YOUR CODE: Save payment.id and other info in your database for later!
