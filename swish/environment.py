from .exceptions import ConfigurationError


class Environment(object):
    def __init__(self, name, base_url, qr_url):
        self.name = name
        self.base_url = base_url
        self.qr_url = qr_url

    def __str__(self):
        return self.name

    @staticmethod
    def parse_environment(environment):
        if isinstance(environment, Environment) or environment is None:
            return environment
        try:
            return Environment.All[environment]
        except KeyError:
            raise ConfigurationError("Provided environment name is invalid")


Environment.MSS = Environment(
    name="mss",
    base_url="https://mss.cpc.getswish.net/swish-cpcapi/api/v1/",
    qr_url=None ## MSS doesn't need or have QR codes
)
Environment.Sandbox = Environment(
    name="sandbox",
    base_url="https://staging.getswish.pub.tds.tieto.com/swish-cpcapi/api/v1/",
    qr_url="https://staging.getswish.pub.tds.tieto.com/qrg-swish/api/v1/"
)
Environment.Production = Environment(
    name="production",
    base_url="https://cpc.getswish.net/swish-cpcapi/api/v1/",
    qr_url="https://mpc.getswish.net/qrg-swish/api/v1/"
)

# deprecated
Environment.Test = Environment(
    name="test",
    base_url="https://mss.cpc.getswish.net/swish-cpcapi/api/v1/",
    qr_url=None
)

Environment.All = {
    "test": Environment.Test,
    "mss": Environment.MSS,
    "sandbox": Environment.Sandbox,
    "production": Environment.Production
}
