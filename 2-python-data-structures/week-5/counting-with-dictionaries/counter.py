# one common use of dictionaries is counting how often we "see" something

cc = dict()
cc["word1"] = 1
cc["word2"] = 1

# print(cc)


cc["word1"] = cc["word1"] + 1
# print(cc)


counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
