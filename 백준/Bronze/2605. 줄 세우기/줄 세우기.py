students_num = int(input())
rule = list(map(int, input().split()))
line = [n for n in range(1, students_num + 1)]

for i in range(students_num):
    n, t = rule[i], line[i]
    for j in range(i, i-n, -1):
        line[j] = line[j-1]
    line[i-n] = t

print(*line)