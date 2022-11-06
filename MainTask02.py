# Specularity vector elements

# Stage #11 (Main task 02)
# Subject theme: Python Basic Syntax. High Level Data Types. Lists
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 06.11.2022
def check_specularity(ls):
    while len(ls) != 0:
        if ls[0] != ls[len(ls) - 1]:
            return False
        ls = ls[1:len(ls) - 1]

    return True


def main():
    ls = list(map(int, list(input(f"Enter vector elements separated by spaces: ").split())))

    print(f"Your vector: {ls}")

    msg = (f"Vector elements are mirrored." if check_specularity(ls)
           else f"Vector elements are not mirrored.")

    print(msg)


main()
