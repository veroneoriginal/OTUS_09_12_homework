def foo(value: int | str) -> int | str:
    return value

if __name__ == "__main__":
    foo("foo")
    foo(1)
    # foo([]) # expect-type-error
