from .exceptions import ConfigurationError


class Environment(object):
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url

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

Environment.Test = Environment(name="test",
                               base_url="http://localhost/")
Environment.Production = Environment(name="production",
                                     base_url="https://swicpc.bankgirot.se/swish-cpcapi/api/v1/")
Environment.All = {
    "test": Environment.Test,
    "production": Environment.Production
}
