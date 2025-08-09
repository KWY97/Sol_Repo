def solution(n, computers):
    answer = 0

    def dfs(graph, N):
        connections = []
        visited = [False] * N

        for start_node in range(N):
            if visited[start_node]:
                continue
            stack = [start_node]
            connection = []

            while stack:
                node = stack.pop()

                if visited[node]:
                    continue

                visited[node] = True
                connection.append(node)

                for next_node in range(N):
                    if node == next_node:
                        continue
                    if visited[next_node]:
                        continue
                    if graph[node][next_node] == 0:
                        continue

                    stack.append(next_node)
            connections.append(connection)
        return connections
        
    ans = dfs(computers, n)
    answer = len(ans)

    return answer