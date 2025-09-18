N = int(input())
plus = 0


for i in range(50, N):
    if '50' in str(i):
        plus += 1

print(N+plus)