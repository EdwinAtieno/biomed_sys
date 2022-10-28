import re
from typing import Any

from django.core.exceptions import ValidationError


def phone_number_validator(value: str) -> Any:
    """
    Validate phone number.
    """

    if re.match(  # noqa W605 type: ignore["return-value"]
        r"^254[0-9]{9}$", value
    ):
        return value

    raise ValidationError("Invalid phone number")


def staff_number_validator(value: str) -> Any:
    """
    Validate staff number.
    """

    if re.match(  # noqa W605 type: ignore["return-value"]
        r"^N[0-9]{6}$", value
    ):
        return value

    raise ValidationError("Invalid staff number")


def asset_number_validator(value: str) -> Any:
    """
    Validate asset number.
    """

    if re.match(  # noqa W605 type: ignore["return-value"]
        r"^NE[0-9]{5}$", value
    ):
        return value

    raise ValidationError("Invalid asset number")
