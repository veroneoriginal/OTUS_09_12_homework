from typing import Final
my_list: Final = []

if __name__ == "__main__":
    my_list.append(1)
    # my_list = [] # expect-type-error
    # my_list = "something else" # expect-type-error
