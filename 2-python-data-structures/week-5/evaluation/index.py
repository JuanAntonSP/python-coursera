handle = open("./mbox-short.txt")

counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        person = words[1]
        counts[person] = counts.get(person, 0) + 1

print(counts)


bigWord = None
bigCount = None

for word, value in counts.items():
    if bigCount is None or value > bigCount:
        bigCount = value
        bigWord = word

print(bigWord, bigCount)
