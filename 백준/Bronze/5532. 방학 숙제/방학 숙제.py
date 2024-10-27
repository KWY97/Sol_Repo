import sys
input = sys.stdin.readline

def math(total_math, day_math):
    day = 0

    while True:
        if total_math <= 0:
            return day

        total_math -= day_math
        day += 1


def korean(total_korean, day_korean):
    day = 0
    
    while True:
        if total_korean <= 0:
            return day
        
        total_korean -= day_korean
        day+=1

L = int(input()) # 방학 총 일수
A = int(input()) # 국어 총 페이지
B = int(input()) # 수학 총 페이지
C = int(input()) # 하루 국어 최대 페이지
D = int(input()) # 하루 수학 최대 페이지

hw_day = max(math(B, D), korean(A, C))
print(L - hw_day)