my_sum = 0
min_num = 101
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        my_sum += num
        if min_num > num:
            min_num = num

if my_sum != 0:
    print(my_sum)
    print(min_num)
else:
    print(-1)