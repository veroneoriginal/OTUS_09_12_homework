from typing import TypeVar

T = TypeVar("T", bound=int)

def add(a: T) -> T:
    return a
