largest = -1

for i in range(10):
    num = int(input("Enter number: "))

    if num % 2 != 0:
        if num > largest:
            largest = num

print("Largest odd number =", largest)