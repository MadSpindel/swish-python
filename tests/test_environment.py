import unittest

from swish.environment import Environment
from swish.exceptions import ConfigurationError


class EnvironmentTestCase(unittest.TestCase):

    def test_parse_environment_string(self):
        environment = Environment.parse_environment("test")
        self.assertEqual(environment, Environment.Test)

    def test_parse_environment_string_error(self):
        with self.assertRaises(ConfigurationError):
            Environment.parse_environment("invalid")

    def test_parse_environment_object(self):
        environment = Environment.parse_environment(Environment.Test)
        self.assertEqual(environment, Environment.Test)
