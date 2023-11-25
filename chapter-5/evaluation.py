smallest = None
largest = None

while True:
    value = input("Enter a number: ")
    if value == "done":
        break

    try:
        value = int(value)
        if smallest is None or value < smallest:
            smallest = value
        if largest is None or value > largest:
            largest = value
    except ValueError:
        print("Invalid input")

print("Max:", largest)
print("Min:", smallest)

