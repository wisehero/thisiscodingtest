def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]< 38:
            continue
        elif grades[i] % 5 < 3:
            continue
        else:
            grades[i] = grades[i] + (5 - (grades[i]% 5))
    return grades
