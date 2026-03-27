def gradingStudents(grades):
    arr = []
    for grade in grades:
        if grade <= 40:
            arr.append(grade)
            continue
        rounded = False
        for i in range(grade, grade+3):
            if i % 5 == 0:
                if i - grade <= 3:
                    arr.append(i)
                    rounded = True
                    break
        if not rounded:
            arr.append(grade)
    return arr

print(gradingStudents([73, 67, 38, 33]))