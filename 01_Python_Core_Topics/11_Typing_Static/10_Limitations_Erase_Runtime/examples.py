"""Notes on type system limitations and runtime erasure."""

from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def is_type(self, expected: type) -> bool:
        return isinstance(self.value, expected)
