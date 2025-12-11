Vector = list[float | int]

def foo(value: Vector):
    return value

if __name__ == "__main__":
    foo([1.1, 2])
    # foo(1) # expect-type-error
    # foo(["1"]) # expect-type-error
