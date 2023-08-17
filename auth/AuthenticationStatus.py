from enum import Enum, auto


class AuthenticationStatus(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    Authenticated = auto()
    Anonymous = auto()
