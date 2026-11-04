# Problem: Grading Students
# Source: https://www.hackerrank.com/challenges/grading/problem
# Note: Rounds student grades up to the next multiple of 5 when the difference is less than 3, provided the grade is at least 38.

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
