text = input()
unique_elements = set()

for ch in text:
    unique_elements.add(ch)

for ch in sorted(unique_elements):
    print(f'{ch}: {text.count(ch)} time/s')
