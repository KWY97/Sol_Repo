def f(n):
    if len(li) == M:
        print(' '.join(map(str, li)))
        return

    for i in range(n, N+1):
        li.append(i)
        f(i)
        li.pop()

N, M = map(int, input().split())
li = []
f(1)