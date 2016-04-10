from schematics import models, types


class Payment(models.Model):
    id = types.StringType()
    payee_payment_reference = types.StringType(serialized_name='payeePaymentReference')
    payment_reference = types.StringType(serialized_name='paymentReference')
    callback_url = types.URLType(serialized_name='callbackUrl')
    payer_alias = types.StringType(serialized_name='payerAlias')
    payee_alias = types.StringType(serialized_name='payeeAlias')
    amount = types.FloatType()
    currency = types.StringType()
    message = types.StringType()
    status = types.StringType()
    date_created = types.DateTimeType(serialized_name='dateCreated')
    date_paid = types.DateTimeType(serialized_name='datePaid')
    location = types.URLType()
    request_token = types.StringType()
    error_code = types.StringType(serialized_name='errorCode')
    error_message = types.StringType(serialized_name='errorMessage')

    class Options:
        serialize_when_none = False


class Refund(models.Model):
    id = types.StringType()
    original_payment_reference = types.StringType(serialized_name='originalPaymentReference')
    amount = types.FloatType()
    currency = types.StringType()
    message = types.StringType()
    payer_alias = types.StringType(serialized_name='payerAlias')
    payee_alias = types.StringType(serialized_name='payeeAlias')
    callback_url = types.URLType(serialized_name='callbackUrl')
    payer_payment_reference = types.StringType(serialized_name='payerPaymentReference')
    payment_reference = types.StringType(serialized_name='paymentReference')
    status = types.StringType()
    date_created = types.DateTimeType(serialized_name='dateCreated')
    date_paid = types.DateTimeType(serialized_name='datePaid')
    location = types.URLType()

    class Options:
        serialize_when_none = False
