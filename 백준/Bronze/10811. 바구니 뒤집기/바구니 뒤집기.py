N, M = map(int, input().split())
arr = []
for temp in range(N+1):
    arr.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    arr[i:j+1] = arr[j:i-1:-1]

print(*(arr[1:]))