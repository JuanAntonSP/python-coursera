# Searching with boolean
found = False

for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    else:
        found = False
    print(found, value)

print("after:", found)