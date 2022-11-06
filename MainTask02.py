def check_specularity(list):
    while len(list) != 0:
        if list[0] != list[len(list) - 1]:
            return False
        list = list[1:len(list) - 1]

    return True


def main():
    list = []
    num_list_elements = int(input(f"Input number of list elements: "))

    for _ in range(num_list_elements):
        list.append(int(input(f"Input element of list: ")))

    print(f"Your vector: {list}")

    msg = (f"Vector elements are mirrored." if check_specularity(list)
           else f"Vector elements are not mirrored.")

    print(msg)


main()
