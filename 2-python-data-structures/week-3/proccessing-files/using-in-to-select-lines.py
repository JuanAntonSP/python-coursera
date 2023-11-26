# Print all the lines that includes '@uct.ac.za' word

file = open("./file-2.txt")
for line in file:
    line = line.strip()
    if not "@uct.ac.za" in line:
        continue
    print(line)
