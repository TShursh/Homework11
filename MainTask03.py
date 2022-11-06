# Аll elements vectors are different/same

# Stage #11 (Main task 03)
# Subject theme: Python Basic Syntax. High Level Data Types. Lists
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 06.11.2022

def check_identical_elements(ls):
    for i in range(len(ls)):
        if ls[i] != ls[i - 1]:
            return False
    return True


def main():
    ls = list(map(int, list(input(f"Enter vector elements separated by spaces: ").split())))

    print(f"Your vector: {ls}")

    if check_identical_elements(ls):
        msg = f"All vector elements are the same."
    else:
        msg = f"The vector elements are the different."

    print(msg)


main()
