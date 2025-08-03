N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
numbers_dict = {}
MAX = max(numbers)
MIN = min(numbers)

avg = int(round(sum(numbers) / N, 0))
mid = numbers[N//2]

for num in numbers:
    numbers_dict[num] = numbers_dict.get(num, 0) + 1

nums = list(numbers_dict.items())
nums.sort(key=lambda kv: (-kv[1], kv[0]))

temp = [[4001] for _ in range(500001)]

for k, v in nums:
    if temp[v] == [4001]:
        temp[v] = [k]
    else:
        temp[v].append(k)

for row in temp:
    if row[0] == 4001:
        continue
    if len(row) == 1:
        many = row[0]
    else:
        many = row[1]


print(avg)
print(mid)
print(many)
print(MAX-MIN)