"""Generic class and function examples."""

from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


class Peekable(Generic[T]):
    def __init__(self, iterable: Iterable[T]):
        self._iter = iter(iterable)
        self._buffer: list[T] = []

    def __iter__(self) -> Iterator[T]:
        for value in self._buffer:
            yield value
        self._buffer.clear()
        yield from self._iter

    def peek(self) -> T:
        if not self._buffer:
            self._buffer.append(next(self._iter))
        return self._buffer[0]
