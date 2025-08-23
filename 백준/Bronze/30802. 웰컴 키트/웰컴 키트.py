# 티: for 문 돌면서
# 원소 % T == 0 이면 cnt에 원소 // T 추가
# 그게 아니면 원소 // T + 1 추가

# 펜: 다 더하고 // P, 다 더하고 % P

N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())
cnt = 0

for size in shirts:
    if size % T == 0:
        cnt += size // T
    else:
        cnt += size // T + 1

print(cnt)
print(N // P, N % P)