import sys
input = sys.stdin.readline

while True:
    n = int(input())
    divisor = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    cnt = len(divisor)
    if sum(divisor) == n:
        print(n, end = " = ")
        for i in range(cnt):
            if i != cnt - 1:
                print(f'{divisor[i]} + ', end = '')
            else:
                print(divisor[i])
    else:
        print(f'{n} is NOT perfect.')