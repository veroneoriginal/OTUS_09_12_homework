def foo(value):
    return value


if __name__ == "__main__":
    print(foo(1))
    print(foo("10"))
    # print(foo(1, 2)) # expect-type-error