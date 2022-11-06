# Even/uneven vector elements.

# Stage #11 (Main task 04)
# Subject theme: Python Basic Syntax. High Level Data Types. Lists
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 06.11.2022

def count_even_value(ls):
    count = 0
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            count += 1

    return count


def count_uneven_value(ls):
    count = 0
    for i in range(len(ls)):
        if ls[i] % 2 == 1:
            count += 1

    return count


def main():
    ls = list(map(int, list(input(f"Enter vector elements separated by spaces: ").split())))

    msg = (f"Vector has {count_even_value(ls)} even elements.\n"
           f"Vector has {count_uneven_value(ls)} uneven elements.")

    print(msg)


main()
