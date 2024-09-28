import sys
input = sys.stdin.readline

N = int(input())
divisor = []
prime_num = []
ans = []
temp = []
prime = False

for i in range(1, N):
    if N % i == 0:
        temp.append(i)
if len(temp) == 1:
    prime = True

if N == 1:
    pass
elif prime == True:
    print(N)
else:
    for i in range(2, N):
        if N % i == 0:
            divisor.append(i)

    for num in divisor:
        temp = []
        for j in range(1, num):
            if num % j == 0:
                temp.append(num)
        if len(temp) == 1:
            prime_num.append(num)

    max_prime = max(prime_num)

    while N >= max_prime:
        for i in prime_num:
            if N % i == 0:
                N //= i
                ans.append(i)
                break
    for i in ans:
        print(i)