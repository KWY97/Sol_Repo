def my_dfs(L, result):
    global ans

    if L == M:
        ans.append(result[:])
        return

    for i in range(N):
            result.append(N_list[i])
            my_dfs(L+1, result)
            result.pop()
    return ans


N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]
ans = []
results = (my_dfs(0, []))

for result in results:
    print(' '.join(map(str, result)))