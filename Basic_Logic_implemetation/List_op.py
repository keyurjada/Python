lst = []

while True:
    print("\n1.Insert")
    print("2.Delete")
    print("3.Display")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        n = int(input("Enter number: "))
        lst.append(n)

    elif ch == 2:
        n = int(input("Enter number to delete: "))
        lst.remove(n)

    elif ch == 3:
        print("List =", lst)

    elif ch == 4:
        break