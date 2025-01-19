nums = input()
arr = []

for num in nums:
    arr.append(int(num))

arr.sort(reverse=True)
print("".join(map(str, arr)))