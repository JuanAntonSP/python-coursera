# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

acc = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    line = line.strip()

    count = count + 1
    pos = line.find(":")
    value = line[pos + 1 :]
    value = value.strip()
    acc = acc + float(value)

result = acc / count
print("Average spam confidence:", result)
