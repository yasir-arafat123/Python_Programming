"""TypedDict, Literal, and Annotated usage examples."""

from typing import Annotated, Literal, TypedDict


class Config(TypedDict):
    mode: Literal["debug", "release"]
    retries: int


TimeoutSeconds = Annotated[float, "seconds"]
