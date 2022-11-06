from random import randint


def find_arithmetic_mean(list):
    sum = 0
    i = len(list) - 1
    while i >= 0:
        sum += list[i]
        i -= 1

    return round(sum / len(list), 2)


def count_positive_value(list):
    i = len(list) - 1
    count = 0
    while i >= 0:
        if list[i] > 0:
            count += 1
        i -= 1

    return count


def count_negative_value(list):
    i = len(list) - 1
    count = 0
    while i >= 0:
        if list[i] < 0:
            count += 1
        i -= 1

    return count


def count_zero_value(list):
    i = len(list) - 1
    count = 0
    while i >= 0:
        if list[i] == 0:
            count += 1
        i -= 1

    return count


def swap_extreme_value(list):
    max_i = list.index(max(list))
    min_i = list.index(min(list))
    list[max_i], list[min_i] = list[min_i], list[max_i]

    return list


def main():
    list = []
    num_list_elements = int(input(f"Input number of list elements: "))

    for i in range(num_list_elements):
        list.append(randint(-100, 100))

    print(f"Your list before changes:       {list}")
    print(f"After replacing extreme values: {swap_extreme_value(list)}")
    print(f"Max --> {max(list)}")
    print(f"Min --> {min(list)}")
    print(f"Arithmetic mean --> {find_arithmetic_mean(list)}")
    print(f"Number of positive elements is {count_positive_value(list)}")
    print(f"Number of negative elements is {count_negative_value(list)}")
    print(f"Number of zero elements is {count_zero_value(list)}")


main()
