max_v = float('-inf')
max_i = 0

for i in range(1, 10):
    temp = int(input())
    if max_v < temp:
        max_v = temp
        max_i = i

print(max_v)
print(max_i)