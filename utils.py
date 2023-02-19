import string
from random import (
    choice,
    randint,
)
from typing import Any


def generate_number(num_digits: int = 6) -> int:
    """
    Generate a pin. of specified length.
    """
    number = 0

    while len(str(number)) != num_digits:
        number = randint(1, (10**num_digits) - 1)

    return number


def generate_asset_number(num_digits: int = 6) -> Any:
    """
    Generate a pin. of specified length.
    """

    res = "".join(choice(string.digits) for x in range(num_digits))
    asset_number = "NE" + res

    return asset_number
