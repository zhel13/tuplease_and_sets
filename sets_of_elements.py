set1_range, set2_range = map(int, input().split())

set1 = set(int(input()) for _ in range(set1_range))
set2 = set(int(input()) for _ in range(set2_range))

result = set1&set2
print(*result, sep='\n')
