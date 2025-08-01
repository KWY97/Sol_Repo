import sys
input = sys.stdin.readline

T = int(input())
N_li = [int(input()) for _ in range(T)]
max_n = max(N_li)

# 한 번만 소수 구해서 모든 N에서 쓰기 : 0..max_n 까지
is_prime = [False, False] + [True] * (max_n - 1)
for i in range(2, int(max_n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_n + 1, i):
            is_prime[j] = False

cnts = []
for N in N_li:
    cnt = 0
    half = N // 2
    for p in range(2, half + 1):
        if is_prime[p] and is_prime[N - p]:
            cnt += 1
    cnts.append(cnt)

for ans in cnts:
    print(ans)