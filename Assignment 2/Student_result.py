marks = []
def inpmark():
    global marks
    marks = []
    n = int(input("How many subjects? "))
    for i in range(n):
        m = float(input(f"Enter marks of subject {i+1}: "))
        marks.append(m)

def calper():
    if len(marks) == 0:
        print("Enter marks first")
        return
    per = sum(marks) / len(marks)
    print("Percentage =", per)
    return per

def assigr():
    per = calper()
    if per is None:
        return

    if per >= 90:
        print("Grade: A+")
    elif per >= 75:
        print("Grade: A")
    elif per >= 60:
        print("Grade: B")
    elif per >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")

while True:
    print("\n1.Enter Marks  2.Calculate Percentage  3.Assign Grade  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        inpmark()
    elif ch == 2:
        calper()
    elif ch == 3:
        assigr()
    elif ch == 4:
        break
    else:
        print("Invalid choice")