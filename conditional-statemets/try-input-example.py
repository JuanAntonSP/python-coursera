val = input("Enter a number:")
try:
    iVal = int(val)
except:
    iVal = -1

if iVal > 0:
    print("nice work")
else:
    print("not a number")