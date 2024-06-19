![swish](https://cloud.githubusercontent.com/assets/3159565/14217729/1d4b6732-f850-11e5-8a00-90d4ab30ddbd.png)

[![Build Status](https://travis-ci.org/MadSpindel/swish-python.svg?branch=master)](https://travis-ci.org/MadSpindel/swish-python)
[![codecov.io](https://codecov.io/github/MadSpindel/swish-python/coverage.svg?branch=master)](https://codecov.io/github/MadSpindel/swish-python?branch=master)
# 💰 Swish Python Client Library
This client library is designed to support the Swish handel API.

[Offical Integration Guide](https://assets.ctfassets.net/zrqoyh8r449h/68UD4zzhqCEVffNDD7G2ko/e53ac6bae9d3608858fd98d58732f336/Merchant_Integration_Guide_2.5.pdf)

## 🏗 Installation
It's easy! Just install it with pip:
```
pip install swish
```
## 📋 Quick Start Example
```python
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
```
