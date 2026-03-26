def facto(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# recursive function of this

def factor(n):
    if n == 0 or n == 1:
        return 1
    return n * factor(n-1)

num = int(input("Enter number: "))
print("Normal Factorial =", facto(num))
print("Recursive Factorial =", factor(num))