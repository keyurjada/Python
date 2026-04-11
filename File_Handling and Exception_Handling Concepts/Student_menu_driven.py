students = {}

while True:
    print("\n1.Add 2.Search 3.List 4.Update 5.Delete 6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Roll No: ")
        name = input("Name: ")
        students[roll] = name

    elif choice == 2:
        roll = input("Enter Roll No: ")
        print(students.get(roll, "Not Found"))

    elif choice == 3:
        for r, n in students.items():
            print(r, n)

    elif choice == 4:
        roll = input("Enter Roll No: ")
        if roll in students:
            students[roll] = input("New Name: ")

    elif choice == 5:
        roll = input("Enter Roll No: ")
        students.pop(roll, None)

    elif choice == 6:
        break