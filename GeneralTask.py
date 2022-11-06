# Operations on a sequence of numbers

# Stage #11 (General task)
# Subject theme: Python Basic Syntax. High Level Data Types. Lists
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 05.11.2022

def find_arithmetic_mean(ls):
    summ = 0
    i = len(ls) - 1
    while i >= 0:
        summ += ls[i]
        i -= 1

    return round(summ / len(ls), 2)


def count_positive_value(ls):
    i = len(ls) - 1
    count = 0
    while i >= 0:
        if ls[i] > 0:
            count += 1
        i -= 1

    return count


def count_negative_value(ls):
    i = len(ls) - 1
    count = 0
    while i >= 0:
        if ls[i] < 0:
            count += 1
        i -= 1

    return count


def count_zero_value(ls):
    i = len(ls) - 1
    count = 0
    while i >= 0:
        if ls[i] == 0:
            count += 1
        i -= 1

    return count


def swap_extreme_value(ls):
    max_i = ls.index(max(ls))
    min_i = ls.index(min(ls))
    ls[max_i], ls[min_i] = ls[min_i], ls[max_i]

    return ls


def main():
    ls = list(map(int, list(input(f"Enter values separated by spaces: ").split())))

    print(f"Your list before changes:       {ls}")
    print(f"After replacing extreme values: {swap_extreme_value(ls)}")
    print(f"Max --> {max(ls)}")
    print(f"Min --> {min(ls)}")
    print(f"Arithmetic mean --> {find_arithmetic_mean(ls)}")
    print(f"Number of positive elements is {count_positive_value(ls)}")
    print(f"Number of negative elements is {count_negative_value(ls)}")
    print(f"Number of zero elements is {count_zero_value(ls)}")


main()
