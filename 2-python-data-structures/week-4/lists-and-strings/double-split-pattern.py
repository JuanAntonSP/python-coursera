file = open("./mbox-short.txt")

# line example
# From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008

for line in file:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    email = words[1]
    pieces = email.split("@")
    print(pieces)
