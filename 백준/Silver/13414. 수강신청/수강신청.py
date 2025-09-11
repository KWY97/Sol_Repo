import sys
input = sys.stdin.readline

K, L = map(int, input().split())
students_li = [input().strip() for _ in range(L)]
students_dict = {}
cnt = 0

for i, v in enumerate(students_li):
    students_dict[v] = i

sorted_students_dict = sorted(students_dict.items(), key = lambda x: x[1])

for student in sorted_students_dict:
    if cnt < K:
        print(student[0])
        cnt += 1
    else:
        break