import unittest

from swish.environment import Environment
from swish.exceptions import ConfigurationError


class EnvironmentTestCase(unittest.TestCase):

    def test_parse_environment_string(self):
        environment = Environment.parse_environment("mss")
        self.assertEqual(environment, Environment.MSS)

    def test_parse_environment_string_error(self):
        with self.assertRaises(ConfigurationError):
            Environment.parse_environment("invalid")

    def test_parse_environment_object(self):
        environment = Environment.parse_environment(Environment.MSS)
        self.assertEqual(environment, Environment.MSS)

    def test_environment_str(self):
        environment = Environment.MSS
        self.assertEqual(str(environment), environment.name)
