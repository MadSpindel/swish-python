class SwishError(Exception):
    def __init__(self, json):
        code = json[0].get('errorCode')
        message = json[0].get('errorMessage')
        super(SwishError, self).__init__(message)
        self.error_code = code
        self.error_message = message


class ConfigurationError(Exception):
    pass
