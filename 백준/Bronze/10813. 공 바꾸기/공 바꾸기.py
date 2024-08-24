N, M = map(int, input().split())

arr = []
for temp in range(N+1):
    arr.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

print(*(arr[1:]))