from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class User:
    name: str


class AuthenticationStatus(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self

    Authenticated = auto()
    Anonymous = auto()
