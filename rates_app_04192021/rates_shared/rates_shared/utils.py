"""Utils Module"""
from typing import Optional, Any
import re
import pathlib
import yaml

CLIENT_COMMAND_PARTS = [
    r"^(?P<name>[A-Z]*) ",
    r"(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}) ",
    r"(?P<symbols>[A-Z,:;|]*)$",
]

CLIENT_COMMAND_REGEX = re.compile("".join(CLIENT_COMMAND_PARTS))


def parse_command(client_command_str: str) -> Optional[dict[str, str]]:
    """ parse command """

    client_command_match = CLIENT_COMMAND_REGEX.match(
        client_command_str)

    if not client_command_match:
        return None

    return client_command_match.groupdict()


def read_config() -> Any:
    """ read config """
    with open(pathlib.Path("config", "rates_config.yaml")) as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.SafeLoader)
