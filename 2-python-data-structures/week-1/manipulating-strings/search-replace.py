# Search and replace
# With replace(), we replace all occurrences
greet = "Hello Juan"
newGreet = greet.replace("Juan", "Bob")
print(newGreet) # output: Hello Bob


# II. Stripping Whitespace
name="  Juan Antonio   "
leftFixedName = name.lstrip()
print(leftFixedName)

rightFixedName = name.rstrip()
print(rightFixedName)

fixedName = name.strip()
print(fixedName)


# III. Prefixes
line = "Please have a nice day"

# Output: True
print(line.startswith("Please"))
 
# Output: False
print(line.startswith("p"))
