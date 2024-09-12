N = int(input())
ans = 3

for i in range(1, N):
    ans = ans + (1 << i)
print(ans**2)