def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
trees = [int(input()) for _ in range(n)]
diffs = []
cnt = 0

for i in range(n-1):
    diffs.append(abs(trees[i+1] - trees[i]))

gcd_diff = diffs[0]

for j in range(1, n-1):
    gcd_diff = gcd(gcd_diff, diffs[j])

min_tree = trees[0]
max_tree = trees[n-1]

cnt = (max_tree - min_tree) // gcd_diff + 1 - n

print(cnt)