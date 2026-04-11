with open("numbers.txt", "r") as file:
    nums = list(map(int, file.read().split()))

print("Total:", sum(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))