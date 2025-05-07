import sys
input = sys.stdin.readline

import copy

a, b = map(int, input().strip().split())

set_a = set(map(int, input().strip().split()))
temp_a = copy.deepcopy(set_a)

set_b = set(map(int, input().strip().split()))


for i in set_b:
    if i in temp_a:
        temp_a.remove(i)

for j in set_a:
    if j in set_b:
        set_b.remove(j)

print(len(temp_a) + len(set_b))