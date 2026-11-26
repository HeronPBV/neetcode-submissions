def add_two_numbers() -> int:
    inputed_numbers = input()
    total = 0
    for num in inputed_numbers.split(","):
        total += int(num)
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
