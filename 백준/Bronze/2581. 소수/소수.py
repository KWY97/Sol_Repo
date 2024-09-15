import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

prime_num = []
for num in range(M, N+1): # 10, 20
    temp = []
    for i in range(1, num):
        if num % i == 0:
            temp.append(i)
    if len(temp) == 1:
        prime_num.append(num)

if not prime_num:
    print(-1)
else:
    print(sum(prime_num))
    print(prime_num[0])