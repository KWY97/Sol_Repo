N, M = map(int, input().split())
arr = [0] * (N+1) # 1번부터 N번 바구니 (인덱스도 1~N)

for _ in range(M):
    i, j, k = map(int, input().split()) # 1부터 시작
    for x in range(i, j+1):
        arr[x] = k

print(*(arr[1:]))