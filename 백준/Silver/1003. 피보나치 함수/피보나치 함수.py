n = int(input())

for _ in range(n):
    num = int(input())

    cnt_zero = [0] * 41
    cnt_one = [0] * 41

    cnt_zero[0], cnt_one[0] = 1, 0
    cnt_zero[1], cnt_one[1] = 0, 1

    for i in range(2, num+1):
        cnt_zero[i] = cnt_zero[i-1] + cnt_zero[i-2]
        cnt_one[i] = cnt_one[i-1] + cnt_one[i-2]

    print(cnt_zero[num], cnt_one[num])