import sys
input = sys.stdin.readline

n = int(input())
ops = [int(input()) for _ in range(n)]
ops.sort()
p = int(n * 0.15 + 0.5)
if n == 0:
    print(0)
else:
    ans = int((sum(ops[p:n-p]) / len(ops[p:n-p])) + 0.5)
    print(ans)
