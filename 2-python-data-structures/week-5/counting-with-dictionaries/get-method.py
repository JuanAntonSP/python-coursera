# to check is a key is already in a dictionary
# simplifying the counting

names = ["csev", "cwen", "csev", "zqian", "cwen"]


counts = dict()
for name in names:
    print(name, counts.get(name, 0))
    counts[name] = counts.get(name, 0) + 1
print(counts)
