# Marks

# Stage #11 (Additional task)
# Subject theme: Python Basic Syntax. High Level Data Types. Lists
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 06.11.2022

# First option (no fool-proof):
# def calculate_percentage(mark, marks):
#     return f"{round(marks.count(mark) * 100 / len(marks), 1)}% ({marks.count(mark)})"
#
#
# def main():
#     print(f"Exam Result Handling")
#     ls = list(map(int, list(input(f"Marks: ").split())))
#
#     msg = (f"fives - {calculate_percentage(5, ls)}\n"
#            f"fours - {calculate_percentage(4, ls)}\n"
#            f"triplets - {calculate_percentage(3, ls)}\n"
#            f"deuces - {calculate_percentage(2, ls)}\n"
#            f"units - {calculate_percentage(1, ls)}\n"
#            f"zeros - {calculate_percentage(0, ls)}\n")
#
#     print(msg)
#
#
# main()

# Second option:
def count_number_occurrences(mark, marks):
    count = 0
    for i in range(len(marks)):
        if mark == marks[i]:
            count += 1
        if not 0 <= marks[i] <= 5:
            return -1
    return count


def main():
    print(f"Exam Result Handling")
    ls = list(map(int, list(input(f"Marks: ").split())))

    cursive_marks = ["zeros", "units", "deuces", "triplets", "fours", "fives"]
    for i in range(len(cursive_marks)):
        result = count_number_occurrences(i, ls)
        if result == -1:
            print(f"Please, enter valid marks (from 0 to 5).")
            break
        print(f"{cursive_marks[i]} - {round(result * 100 / len(ls), 2)}% ({result})")


main()
