size = 5
arr = [list(input()) for _ in range(size)]

max_len = 0
for i in range(size):
    if max_len < len(arr[i]):
        max_len = len(arr[i])

for j in range(max_len): # 0~5
    for i in range(size): # 0~4
        if len(arr[i]) <= j: continue
        print(arr[i][j], end = "")