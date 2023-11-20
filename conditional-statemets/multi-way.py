x = 0
if x < 2:
    print ('small')
elif x < 10 :
    print ('Medium' )
else :
    print ('LARGE ')
print ('All done')


# example 2
x=15
if x < 2:
    print ('Small')
elif x < 10 :
    print ('Medium')
elif x < 20 :
    print ('Big')
elif x < 40 :
    print ('Large')
elif x < 100:
    print ('Huge')
else:
    print ('Ginormous')


# example 3
value = "hello Juan"
try:
    iValue = int(value)
except:
    iValue=-1
print("First Value", iValue)

# example 3
value = "123"
try:
    iValue = int(value)
except:
    iValue=-1
print("Other Value", iValue)


# example 5
astr = 'Bob'
try:
    # this will be displayed
    print ('Hello')
    istr = int(astr)
    # this will not be displayed
    print ('There')
except:
    istr = -1

print ('Done', istr)