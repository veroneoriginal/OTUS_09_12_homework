from typing import TypeVar

T = TypeVar("T", int, str)

def add(a: T, b: T) -> T:
    return a + b
