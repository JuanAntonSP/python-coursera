fname = input("Enter file name: ")
fh = open(fname)
newList = list()

for line in fh:
    wordsInLine = line.split()
    for word in wordsInLine:
        if word not in newList:
            newList.append(word)

finalList = sorted(newList)
print(finalList)
