"""Examples of Protocol usage and runtime checks."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsClose(Protocol):
    def close(self) -> None: ...


def shutdown(resource: SupportsClose) -> None:
    resource.close()
