# fname = input("Enter file name: ")
fh = open("./mbox-short.txt")
newList = list()

count = 0
for line in fh:
    if line.startswith("From "):
        count = count + 1
        words = line.split()
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
