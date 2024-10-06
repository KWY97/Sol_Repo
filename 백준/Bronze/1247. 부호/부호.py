ts = 3
for _ in range(ts):
    N = int(input())
    my_sum = 0
    for _ in range(N):
        my_sum += int(input())
    if my_sum == 0:
        print(0)
    elif my_sum > 0:
        print('+')
    else:
        print('-')