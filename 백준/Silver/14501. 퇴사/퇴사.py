def my_dfs(n, total_cost):
    global ans
    if n >= N:
        ans = max(ans, total_cost)
        return

    if n+T[n] <= N:
        my_dfs(n+T[n], total_cost + P[n])
    my_dfs(n+1, total_cost)

    return ans


N = int(input())
T = [0] * N
P = [0] * N
ans = 0

for i in range(N):
    T[i], P[i] = map(int, input().split())

print(my_dfs(0, 0))