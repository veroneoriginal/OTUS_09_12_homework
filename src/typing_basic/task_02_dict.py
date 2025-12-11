def foo(value: dict[str, str]) -> dict:
    """
    Takes one argument of dict type.
    Keys and values must be str.
    """
    return value


if __name__ == "__main__":
    print(foo({"a": "bar"}))
    # print(foo({"a": 1})) # expect-type-error