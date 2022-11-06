def check_sorting_ascending(list):
    i = len(list) - 1
    while i > 0:
        if list[i] <= list[i - 1]:
            return False
        i -= 1
    return True


def check_sorting_descending(list):
    i = len(list) - 1
    while i > 0:
        if list[i] >= list[i - 1]:
            return False
        i -= 1
    return True


def main():
    list = []
    num_list_elements = int(input(f"Input number of list elements: "))

    for _ in range(num_list_elements):
        list.append(int(input(f"Input element of list: ")))

    print(f"Your vector: {list}")

    if check_sorting_ascending(list):
        msg = f"The elements of the vector are sorted in ascending order."
    elif check_sorting_descending(list):
        msg = f"The elements of the vector are sorted in descending order."
    else:
        msg = f"Vector elements do not form a sequence."

    print(msg)


main()
