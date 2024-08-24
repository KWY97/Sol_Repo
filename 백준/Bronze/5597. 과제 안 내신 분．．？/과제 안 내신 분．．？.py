student = []
for num in range(1, 31):
    student.append(num)

for _ in range(28):
    n = int(input())
    student.remove(n)

print(student[0])
print(student[1])