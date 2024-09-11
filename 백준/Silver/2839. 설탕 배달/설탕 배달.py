import sys
input = sys.stdin.readline

def my_dfs(n, sum):
    global ans

    if sum > N:
        return

    if sum == N:
        ans = n
        return

    if n >= ans:
        return

    if ans == 1667:
        if sum + 5 <= N:
            my_dfs(n+1, sum + 5)
        if sum + 3 <= N:
            my_dfs(n+1, sum + 3)

N = int(input())
ans = 1667
my_dfs(0, 0)

if ans != 1667:
    print(ans)
else:
    print(-1)