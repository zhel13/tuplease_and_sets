input_range = int(input())
unique_elements = set()

for _ in range(input_range):
    element = input().split()
    for e in range(len(element)):
        unique_elements.add(element[e])

print('\n'.join(unique_elements))


