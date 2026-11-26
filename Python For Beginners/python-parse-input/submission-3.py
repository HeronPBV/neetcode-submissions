from typing import List

def read_integers() -> List[int]:
    integers = input()
    string_list = integers.split(",")
    integer_list = []
    for item in string_list:
        integer_list.append(int(item))
    return integer_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
