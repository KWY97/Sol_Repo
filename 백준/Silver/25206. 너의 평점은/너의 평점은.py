grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

N = 20
grade_info = [list(input().split()) for _ in range(N)]
total = 0
denominator = 0
for i in range(N):
    if grade_info[i][2] == 'P':
        continue
    denominator += float(grade_info[i][1])
    total += float(grade_info[i][1]) * grade[grade_info[i][2]]
print(total/denominator)