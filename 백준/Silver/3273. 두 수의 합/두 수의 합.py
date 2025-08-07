n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
count = 0
numbers.sort()

left = 0
right = n-1

while left < right:
    temp = numbers[left] + numbers[right]
    if temp == x:
        count += 1
        left += 1
    elif temp > x:
        right -= 1
    else: left += 1

print(count)