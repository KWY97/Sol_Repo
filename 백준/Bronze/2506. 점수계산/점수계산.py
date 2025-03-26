import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
result = 0
plus = 0
flag = 0
temp = 0

for i in range(N):
    if scores[i] == 1:
        if flag == 1:
            plus = temp + 1
            result += plus
            temp += 1
        else:
            result += 1
            temp += 1
            flag = 1
    else:
        flag = 0
        temp = 0

print(result)