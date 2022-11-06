# Sorting vector elements

# Stage #11 (Main task 01)
# Subject theme: Python Basic Syntax. High Level Data Types. Lists
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 06.11.2022
def check_sorting_ascending(ls):
    i = len(ls) - 1
    while i > 0:
        if ls[i] <= ls[i - 1]:
            return False
        i -= 1
    return True


def check_sorting_descending(ls):
    i = len(ls) - 1
    while i > 0:
        if ls[i] >= ls[i - 1]:
            return False
        i -= 1
    return True


def main():
    ls = list(map(int, list(input(f"Enter vector elements separated by spaces: ").split())))

    if check_sorting_ascending(ls):
        msg = f"The elements of the vector are sorted in ascending order."
    elif check_sorting_descending(ls):
        msg = f"The elements of the vector are sorted in descending order."
    else:
        msg = f"Vector elements do not form a sequence."

    print(msg)


main()
