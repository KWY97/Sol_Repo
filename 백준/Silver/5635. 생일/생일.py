import sys
input = sys.stdin.readline

N = int(input())

young_name = ""
old_name = ""

max_year = 0
max_month = 0
max_day = 0

min_year = 2011
min_month = 13
min_day = 32

for _ in range(N):
    # student_info[1], [2], [3]은 int형 변환 필요
    student_info = list(input().split())
    
    # 가장 어린 사람 찾기
    # 년도 비교
    if max_year < int(student_info[3]):
        young_name = student_info[0]
        max_year = int(student_info[3])
        max_month = int(student_info[2])
        max_day = int(student_info[1])
    elif max_year == int(student_info[3]):
        # 월 비교
        if max_month < int(student_info[2]):
            young_name = student_info[0]
            max_month = int(student_info[2])
            max_day = int(student_info[1])
        elif max_month == int(student_info[2]):
            # 일 비교
            if max_day < int(student_info[1]):
                young_name = student_info[0]
                max_day = int(student_info[1])
    
    # 가장 나이 많은 사람 찾기
    # 년도 비교
    if min_year > int(student_info[3]):
        old_name = student_info[0]
        min_year = int(student_info[3])
        min_month = int(student_info[2])
        min_day = int(student_info[1])
    elif min_year == int(student_info[3]):
        # 월 비교
        if min_month > int(student_info[2]):
            old_name = student_info[0]
            min_month = int(student_info[2])
            min_day = int(student_info[1])
        elif min_month == int(student_info[2]):
            # 일 비교
            if min_day > int(student_info[1]):
                old_name = student_info[0]
                min_day = int(student_info[1])

print(young_name)
print(old_name)