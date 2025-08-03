import sys
input = sys.stdin.readline

N = int(input())
MAX = 1001
arr = [[0] * MAX for _ in range(MAX)]
paper_cnts = [0] * (N+1)

for paper_no in range(1, N+1):
    x, y, w, h = map(int, input().split())

    for i in range(y, y + h):
        for j in range(x, x + w):
            arr[i][j] = paper_no

for line in arr:
    for no_paper in line:
        paper_cnts[no_paper] += 1

print('\n'.join(map(str, paper_cnts[1:])))