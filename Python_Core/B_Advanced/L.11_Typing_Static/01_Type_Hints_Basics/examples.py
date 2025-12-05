"""Introductory examples of Python type annotations."""

from typing import List, Optional


def greet(name: str, excited: bool = False) -> str:
    suffix = "!" if excited else "."
    return f"Hello, {name}{suffix}"


def average(values: List[float]) -> Optional[float]:
    if not values:
        return None
    return sum(values) / len(values)
