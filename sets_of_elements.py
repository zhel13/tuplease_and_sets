set1_range, set2_range = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(set1_range):
    set1.add(int(input()))
for _ in range(set2_range):
    set2.add(int(input()))

result = set1&set2
print(*result, sep='\n')
