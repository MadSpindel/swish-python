![swish](https://cloud.githubusercontent.com/assets/3159565/14217729/1d4b6732-f850-11e5-8a00-90d4ab30ddbd.png)

[![Build Status](https://travis-ci.org/playing-se/swish-python.svg?branch=master)](https://travis-ci.org/playing-se/swish-python)
[![codecov.io](https://codecov.io/github/playing-se/swish-python/coverage.svg?branch=master)](https://codecov.io/github/playing-se/swish-python?branch=master)
# Swish Python Client Library
This client library is designed to support the [Swish API](https://www.getswish.se/content/uploads/2015/06/Guide-Swish-API_160329.pdf). It was originally developed at [Playing](https://playing.se/).

## Installation
Not available yet.

## Quick Start Example

    import swish

    swish_client = swish.SwishClient(
        environment=swish.Environment.Test,
        payee_alias='1231181189',
        cert=('/path/to/cert.pem', '/path/to/key.pem')
    )

    payment = swish_client.payment_request(
        amount=123,
        currency='SEK',
        callback_url='https://your-callback.url/here/',
        payment_reference='Optional custom reference',
        message='Quick Start Example'
    )

    # YOUR CODE: Save payment.id and other info in your database for later!
