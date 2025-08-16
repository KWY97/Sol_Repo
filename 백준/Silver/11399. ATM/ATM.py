N = int(input())
times = list(map(int, input().split()))
times.sort()
ans = 0
cnt = N

for time in times:
    ans += (time * cnt)
    cnt -= 1

print(ans)