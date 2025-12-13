from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable[..., object])

def decorator(func: F) -> F:
    return func