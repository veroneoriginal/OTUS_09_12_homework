from typing import TypedDict, Unpack, cast


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]) -> None:
    return None


p: Person = Person(name="Capy", age=24)
foo(**p)
foo(**cast(Person, {"name": "Capy", "age": 24}))
# foo(**{"name": "Capy"})
