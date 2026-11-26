from typing import List

def read_integers() -> List[int]:
    integers = input()
    string_list = integers.split(",")
    integer_list = []
    for i in range(len(string_list)):
        integer_list.append(int(string_list[i]))
    return integer_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
