def get_grade_point(g):
    if g == 'A+':
        return 4.5
    elif g == 'A0':
        return 4.0
    elif g == 'B+':
        return 3.5
    elif g == 'B0':
        return 3.0
    elif g == 'C+':
        return 2.5
    elif g == 'C0':
        return 2.0
    elif g == 'D+':
        return 1.5
    elif g == 'D0':
        return 1.0
    else:
        return 0.0


point_and_grade_sums = 0
point_sums = 0

for _ in range(20):
    course, point, grade = input().split()

    if grade == 'P':
        continue

    point = int(float(point))

    point_and_grade_sums += point * get_grade_point(grade)
    point_sums += point

print(point_and_grade_sums / point_sums)
