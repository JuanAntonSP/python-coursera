# Finding the average in a loop
count = 0
sum = 0

for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)

print("average:", sum/count)