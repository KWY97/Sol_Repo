n = int(input())
n_nums = list(map(int, input().split()))
n_nums.sort()

m = int(input())
m_nums = list(map(int, input().split()))

for num in m_nums:
    left = 0
    right = n-1
    flag = 1

    while left <= right:
        mid = (left + right) // 2

        if n_nums[mid] == num:
            flag = 0
            print(1)
            break
        elif n_nums[mid] > num:
            right = mid - 1
        elif n_nums[mid] < num:
            left = mid + 1
    if flag:
        print(0)