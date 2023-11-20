# simple expressions
xx = 2
xx = xx + 2

print(xx)


yy = 404 * 2 
print(yy)

# module
jj = 23
kk =  jj % 5
print(kk)

## double asterik
print(2 ** 3)

## asking types to python
value = "hello"
print(type(value))
print(type(1))


## prohibited operations
#errorValue = "hello" + 1 # output : TypeError: can only concatenate str (not "int") to str

# Several types of numbers
# integers: -14, -2, 0, 1, 404543

# floating point numbers: have decimal parts
# -2.5, 0.0, 98.6

print(type(-2.5)) # output = <class 'float'>


# Typeconversions
# convert integer to float
print(float(100)+ 50) # output = 150.0 

print(type(float(1)))

# integer division 
# produces a floating point result
# note: in python2 the integer division is different
print(10/2)


# string conversion
stringVal = '123'
#print(stringVal + 1) # output= TypeError: can only concatenate str (not "int") to str


intVal = int(stringVal)
print(type(intVal)) # output = <class 'int'>

# nsv = 'hello juan'
# niv = int(nsv)


# user input
name = input("Write your name:")
print("Hello", name)