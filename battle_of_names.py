number_of_names = int(input())
odd_set = set()
even_set = set()
final_result = set()

result = 0

for i in range(1, number_of_names+1):
    name = input()
    for ch in name:
        result += ord(ch)

    result = result // i

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)
    result = 0
if sum(odd_set) == sum(even_set):
    final_result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    final_result = odd_set.difference(even_set)
else:
    final_result = even_set.symmetric_difference(odd_set)

print(*final_result, sep=', ')