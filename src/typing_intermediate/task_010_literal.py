from typing import Literal

def foo(direction: Literal["left", "right"]) -> str:
    return direction

print(foo("left"))
print(foo("right"))

a = "".join(["l", "e", "f", "t"])
# print(foo(a))

