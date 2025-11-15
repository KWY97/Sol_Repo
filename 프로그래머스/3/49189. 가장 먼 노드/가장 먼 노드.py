from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(s):
        q = deque([s])
        dist = [False] * (n+1)
        dist[s] = 0
        
        while q:
            cur_v = q.popleft()
            
            for next_v in graph[cur_v]:
                if dist[next_v] == False:
                    dist[next_v] = dist[cur_v] + 1
                    q.append(next_v)
                    
        return dist[1:]

    dist = bfs(1)
    dist[0] = 0
    max_v = max(dist)
    cnt = 0
    print(dist)
    for v in dist:
        if v == max_v:
            cnt += 1  
    
    return cnt