with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        roll = data[0]
        name = data[1]
        marks = list(map(int, data[2:]))

        total = sum(marks)
        percent = total / len(marks)

        if percent >= 75:
            grade = "A"
        elif percent >= 60:
            grade = "B"
        elif percent >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print(roll, name, total, percent, grade)