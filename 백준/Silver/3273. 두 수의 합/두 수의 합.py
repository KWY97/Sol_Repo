def solution(n, numbers, x):
    ans = 0
    numbers.sort()

    left = 0
    right = n-1

    while left < right:
        temp = numbers[left] + numbers[right]

        if temp == x:
            ans += 1
            left += 1
        elif temp < x:
            left += 1
        else:
            right -= 1

    return ans

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

print(solution(n, numbers, x))