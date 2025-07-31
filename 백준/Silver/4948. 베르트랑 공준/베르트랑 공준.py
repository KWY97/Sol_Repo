import sys
input = sys.stdin.readline

max_num = 123456 * 2

is_prime = [True] * (max_num + 1)
is_prime[0] = is_prime[1] = False
prefix = [0] * (max_num + 1)

for i in range(2, int(max_num ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, max_num + 1, i):
            is_prime[j] = False

for i in range(1, max_num + 1):
    prefix[i] = prefix[i-1] + (1 if is_prime[i] else 0)


while True:
    n = int(input())

    if n == 0:
        break

    cnt = prefix[2*n] - prefix[n]
    print(cnt)