import sys
input = sys.stdin.readline

N = int(input())
student_info = []

for _ in range(N):
    # 이름, 년, 월, 일 받기기
    n, d, m, y = input().split()
    # 년 월, 일 인트형 변환
    d, m, y = map(int, (d, m, y))
    student_info.append([y, m, d, n])

student_info.sort()

print(student_info[-1][3])
print(student_info[0][3])