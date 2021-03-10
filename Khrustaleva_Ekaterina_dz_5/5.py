src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique = set()
seen = set()
for el in src:
    if el not in seen:
        unique.add(el)
    else:
        unique.discard(el)
    seen.add(el)

unique_ordered = [item for item in src if item in unique]
print(unique_ordered)
