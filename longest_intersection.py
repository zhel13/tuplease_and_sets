number_of_lines = int(input())
longest_intersection = {}

for _ in range(number_of_lines):
    first_set_range, second_set_range = input().split("-")
    start_first_set, end_first_set = first_set_range.split(",")
    start_second_set, end_second_set = second_set_range.split(",")

    first_set = set(range(int(start_first_set), int(end_first_set) + 1))
    second_set = set(range(int(start_second_set), int(end_second_set) + 1))
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")

