arr = []
sum = 0

for i in range(1, 46):
    for _ in range(i):
        arr.append(i)

start, end = map(int, input().split())
section_arr = arr[start - 1:end]

for num in section_arr:
    sum += num
print(sum)