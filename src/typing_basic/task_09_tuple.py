def foo(value: tuple[str, int]) -> tuple[str, int]:
    return value


if __name__ == "__main__":
    foo(("foo", 1))

    # foo((1, 2)) # expect-type-error
    # foo(("foo", "bar")) # expect-type-error
    # foo((1, "bar")) # expect-type-error
