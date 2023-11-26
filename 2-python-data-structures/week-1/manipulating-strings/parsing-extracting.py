data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atPos = data.find("@")

print(atPos) # output: the counter begins at zero

# find space after the @ position
spacePos = data.find(" ", atPos)
print(spacePos)


# slice using positions
host = data[atPos+1 : spacePos]
print(f"==>> host: {host}")

