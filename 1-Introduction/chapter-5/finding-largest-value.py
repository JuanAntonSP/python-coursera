# making smart loops
print("Before")
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print("After")


# what is the largest number

print("Finding")
largest = -1
for num in [9, 41, 12, 3, 74, 15]:

    if num > largest:
        largest = num

print("Largest number", largest)
