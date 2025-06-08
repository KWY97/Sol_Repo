def search(array, N):
    start = 1
    end = max(array)

    while start <= end:
        mid = (start + end) // 2
        line_cnt = 0

        for line in array:
            line_cnt += line // mid

        if line_cnt >= N:
            start = mid + 1
        else:
            end = mid - 1

    return end


lines = []
K, N = map(int, input().split())
for _ in range(K):
    line = int(input())
    lines.append(line)

print(search(lines, N))
