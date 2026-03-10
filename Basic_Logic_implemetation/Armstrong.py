for i in range(10):
    num = int(input("Enter number: "))
    temp = num
    s = 0

    while temp > 0:
        d = temp % 10
        s = s + d*d*d
        temp = temp // 10

    if num == s:
        print(num, "is Armstrong number")