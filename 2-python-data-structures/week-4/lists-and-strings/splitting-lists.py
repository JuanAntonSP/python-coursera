abc = "With three words"
stuff = abc.split()

print(stuff)

size = len(stuff)
print(size)

print(stuff[0])


for word in stuff:
    print(word)


line = "A lot                 of spaces"

# with out delimiter, spaces are treated like a delimiter
etc = line.split()
print(etc)  # ['A', 'lot', 'of', 'spaces']

print(len(etc))  # 4


newLine = "first;second;third"
thing = newLine.split(";")
print(thing)  # ['first', 'second', 'third']
print(len(thing))  # 3
