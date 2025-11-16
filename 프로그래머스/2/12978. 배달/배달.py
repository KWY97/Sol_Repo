import sys, heapq
input = sys.stdin.readline


def solution(N, road, K):
    def dijkstra(s):
        dist = [INF] * (N+1)
        dist[s] = 1
        pq = []
        heapq.heappush(pq, (0, s))
        
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            
            if dist[cur_node] < cur_cost:
                continue
            
            for next_node, cost in graph[cur_node]:
                next_cost = cur_cost + cost
                
                if dist[next_node] > next_cost:
                    dist[next_node] = next_cost
                    heapq.heappush(pq, (next_cost, next_node))
        
        return dist[1:]
        
    
    graph = [[] for _ in range(N+1)]
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    INF = 500000
    ans = dijkstra(1)
    cnt = 0
    
    for i in range(N):
        if ans[i] <= K:
            cnt += 1
    
    return cnt