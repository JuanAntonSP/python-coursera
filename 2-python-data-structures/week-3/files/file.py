
file = open("./file.txt")
print(file) # object


dir(file)
content = file.read()
print(f"==>> content: {content}")
# output
# line 1
# line 2
# line 3
# line 4