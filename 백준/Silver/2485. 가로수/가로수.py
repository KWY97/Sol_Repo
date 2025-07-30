import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
trees = [int(input()) for _ in range(n)]
cnt = 0

gcd_diff = trees[1] - trees[0]

for j in range(2, n):
    gcd_diff = gcd(gcd_diff, trees[j] - trees[j-1])

min_tree = trees[0]
max_tree = trees[-1]

cnt = (max_tree - min_tree) // gcd_diff + 1 - n

print(cnt)