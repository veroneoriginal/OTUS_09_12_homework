from typing import TypedDict, NotRequired

class Person(TypedDict):
    name: str
    age: NotRequired[int]
    gender: NotRequired[str]
    address: NotRequired[str]
    email: NotRequired[str]


a: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Male",
    "address": "earth",
    "email": "capy@bara.com",
}

b: Person = {
    "name": "Capy",
}

# v: Person = {
#     "age": 1,
#     "gender": "Male",
#     "address": "earth",
#     "email": "capy@bara.com",
# }