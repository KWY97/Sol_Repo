N = int(input())
A = list(map(int, input().split()))

min_v = float('inf')
max_v = float('-inf')

for v in A:
    if v < min_v:
        min_v = v
    if v > max_v:
        max_v = v

print(min_v, max_v)