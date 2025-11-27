"""Examples of validating types at runtime."""

from typing import Any


def validate_customer(record: dict[str, Any]) -> None:
    required = {"id": int, "email": str}
    for key, expected in required.items():
        if key not in record or not isinstance(record[key], expected):
            raise TypeError(f"Invalid field {key!r}")
