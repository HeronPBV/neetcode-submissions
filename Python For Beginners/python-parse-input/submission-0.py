from typing import List

def read_integers() -> List[int]:
    integers = input()
    integers_str_list = integers.split(",")
    integers_list = []
    for integer in integers_str_list:
        integers_list.append(int(integer))
    return integers_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
