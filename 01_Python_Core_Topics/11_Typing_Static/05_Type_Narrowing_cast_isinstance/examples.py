"""Examples of type narrowing with isinstance and typing.cast."""

from typing import Optional, cast


def read_config(value: object) -> Optional[str]:
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode()
    return None


def force_str(value: object) -> str:
    return cast(str, value)
