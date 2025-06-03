import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
result = 0

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    total_wood = 0

    for tree in trees:
        if tree > mid:
            total_wood += (tree - mid)
        if total_wood >= M:
            break

    if total_wood < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)