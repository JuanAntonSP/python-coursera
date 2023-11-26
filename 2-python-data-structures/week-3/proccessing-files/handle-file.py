print("start")
xfile = open("./file.txt")
for line in xfile:
    print(line)
print("end")

# Reading the whole file
zFile = open("./file.txt")
inp = zFile.read()
inp = print(len(inp))  # includes newline characters

# searching through a file
yFile = open("./file.txt")
for line in yFile:
    if line.startswith("description"):
        print(line)

# Notes
# each line from the file
# has a newline at the end, so the print
# statement adds a newline to each line , and count it


# Searching through a file : version 1
# this version includes newline as a result of the search
rfile = open("./new-file.txt")
for line in rfile:
    if line.startswith("From: "):
        print(line)


# Searching through a file : version 2
# this version ignore the "white space"
rfile = open("./new-file.txt")
for line in rfile:
    line = line.strip()
    if line.startswith("From: "):
        print(line)
