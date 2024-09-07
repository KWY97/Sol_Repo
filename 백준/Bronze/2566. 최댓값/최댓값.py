size = 9
arr = [list(map(int, input().split())) for _ in range(size)]
max_value = 0
max_i, max_j = 0, 0

for i in range(size):
    for j in range(size):
        if max_value < arr[i][j]:
            max_value = arr[i][j]
            max_i, max_j = i, j

print(max_value)
print(max_i+1, max_j+1)