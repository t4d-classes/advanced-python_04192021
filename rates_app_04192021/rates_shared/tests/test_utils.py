""" Test Utils Module """

from unittest import TestCase, main
from unittest.mock import patch, mock_open
import pathlib

from rates_shared.utils import parse_command, read_config

yaml_config = """server:
  host: 127.0.0.1
  port: 5000
database:
  server: localhost\\SQLExpress
  database: somedb
  username: user
  password: pass"""


class TestUtils(TestCase):
    """ Test Utils Class """

    def test_parse_command(self) -> None:
        """ Parse Command Test """

        client_command = "GET 2021-04-01 CAD"

        result = parse_command(client_command)

        self.assertEqual(result, {
            "name": "GET",
            "date": "2021-04-01",
            "symbols": "CAD"
        })

    def test_parse_command_invalid_format(self) -> None:
        """ Parse Command Test """

        client_command = "JUNK"

        result = parse_command(client_command)

        self.assertEqual(result, None)

    def test_read_config(self) -> None:
        """ Read Config Test """

        with patch('rates_shared.utils.open',
                   mock_open(read_data=yaml_config)) as m:

            config = read_config()

            self.assertEqual(config, {
                "server": {
                    "host": "127.0.0.1",
                    "port": 5000,
                },
                "database": {
                    "server": "localhost\\SQLExpress",
                    "database": "somedb",
                    "username": "user",
                    "password": "pass",
                }
            })

            m.assert_called_once_with(
                pathlib.Path(
                    "config",
                    "rates_config.yaml"))


if __name__ == "__main__":
    main()
