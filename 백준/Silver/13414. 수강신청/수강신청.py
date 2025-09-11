import sys
input = sys.stdin.readline

K, L = map(int, input().split())
students_dict = {}
cnt = 0

for _ in range(L):
    v = input().strip()
    if v in students_dict:
        del students_dict[v]
    students_dict[v] = True


for student in students_dict:
    if cnt < K:
        print(student)
        cnt += 1
    else:
        break