number_of_lines = int(input())
longest_intersection = []
first_set = set()
second_set = set()


for _ in range(number_of_lines):
    first_set_range, second_set_range = input().split("-")
    start_first_set, end_first_set = first_set_range.split(",")
    start_second_set, end_second_set = second_set_range.split(",")

    for i in range(int(start_first_set), int(end_first_set) + 1):
        first_set.add(i)
    for j in range(int(start_second_set), int(end_second_set) + 1):
        second_set.add(j)
    if len(longest_intersection) < len(first_set.intersection(second_set)):
        longest_intersection = first_set.intersection(second_set)
    first_set.clear()
    second_set.clear()
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")

