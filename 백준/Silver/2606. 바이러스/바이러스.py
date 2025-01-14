def DFS(computer):
    visited[1] = 1 # 1번 컴퓨터 부터 바이러스 감염 시작
    v = 1

    while True:
        for w in computer_connection[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

computer = int(input())
line = int(input())

computer_connection = [[] for _ in range(computer + 1)]
visited = [0] * (computer + 1)
stack = []
cnt = 0

for _ in range(line):
    start_idx, end_idx = map(int, input().split())
    computer_connection[start_idx].append(end_idx)
    computer_connection[end_idx].append(start_idx)

DFS(computer)

for search_idx in range(2, computer+1):
    if visited[search_idx] == 1:
        cnt += 1

print(cnt)