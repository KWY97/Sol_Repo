from collections import defaultdict

N = int(input())
temp_towers = {}
start_idx = 1001
end_idx = 0
max_idx = 0
max_h = 0
ans = 0

for _ in range(N):
    idx, h = map(int, input().split())
    temp_towers[idx] = h

    if start_idx > idx:
        start_idx = idx
    if end_idx < idx:
        end_idx = idx
    if max_h < h:
        max_h = h
        max_idx = idx

towers = dict(sorted(temp_towers.items(), key= lambda x: x[0]))

# 앞에서 -> 가장 높은 곳
cur_h = 0
for i in range(start_idx, max_idx+1):
    if i not in towers:
        ans += cur_h
    else:
        if cur_h < towers[i]:
            cur_h = towers[i]
        ans += cur_h

# 뒤에서 -> 가장 높은 곳
cur_h = 0
for i in range(end_idx, max_idx-1, -1):
    if i not in towers:
        ans += cur_h
    else:
        if cur_h < towers[i]:
            cur_h = towers[i]
        ans += cur_h

ans -= max_h
print(ans)