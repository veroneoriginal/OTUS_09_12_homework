def foo(x: tuple[()]) -> None:
    pass


if __name__ == "__main__":
    foo(())
    # foo((1,))
