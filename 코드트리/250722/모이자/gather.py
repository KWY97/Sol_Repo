import sys

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
ans = sys.maxsize

for i in range(n):
    point = A[i]
    temp = 0

    for j in range(n):
        d = abs(j-i)

        temp += A[j] * d

    if ans > temp:
        ans = temp

print(ans)