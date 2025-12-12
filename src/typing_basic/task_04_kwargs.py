from typing import TypedDict, Unpack

class FooKwargs(TypedDict):
    a: int
    b: str

def foo(**kwargs: Unpack[FooKwargs]) -> None:
    ...

if __name__ == "__main__":
    foo(a=1, b="2")
    # foo(a=[1]) # expect-type-error
