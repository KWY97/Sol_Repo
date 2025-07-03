nums = []

for _ in range(5):
    n = int(input())
    nums.append(n)

for num in nums:
    if nums.count(num) % 2 != 0:
        print(num)
        break