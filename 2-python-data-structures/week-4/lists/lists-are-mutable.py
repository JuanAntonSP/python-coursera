# Lists are Mutable


## String are not mutable

fruit = "Banana"
# fruit[0] = "b"
# print(fruit)
# TypeError: 'str' object does not support item assignment


## list is mutable
x = fruit.lower()
print(x)

values = [1, 2, 4, 5, 6]
print(f"==>> values: {values}")


values[1] = 10
print(values)  # [1, 10, 4, 5, 6]
