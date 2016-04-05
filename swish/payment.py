from schematics.models import Model
from schematics.types import StringType, URLType, DateTimeType, FloatType


class Payment(Model):
    id = StringType()
    payee_payment_reference = StringType(serialized_name='payeePaymentReference')
    payment_reference = StringType(serialized_name='paymentReference')
    callback_url = URLType(serialized_name='callbackUrl')
    payer_alias = StringType(serialized_name='payerAlias')
    payee_alias = StringType(serialized_name='payeeAlias')
    amount = FloatType()
    currency = StringType()
    message = StringType()
    status = StringType()
    date_created = DateTimeType(serialized_name='dateCreated')
    date_paid = DateTimeType(serialized_name='datePaid')
    location = URLType()
    request_token = StringType()
    error_code = StringType(serialized_name='errorCode')
    error_message = StringType(serialized_name='errorMessage')

    class Options:
        serialize_when_none = False
