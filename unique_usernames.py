uniques_usernames = set()

for _ in range(int(input())):
    uniques_usernames.add(input())

result = '\n'.join(uniques_usernames)
print(result)
