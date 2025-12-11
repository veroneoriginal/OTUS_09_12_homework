from typing import assert_type

def foo(x: int = 1) -> int:
    return x

if __name__ == "__main__":
    assert_type(foo(), int)
    # assert_type(foo(), str) # expect-type-error
