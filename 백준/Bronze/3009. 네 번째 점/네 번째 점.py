li_1 = []
li_2 = []
ans_n = 0
ans_m = 0

for _ in range(3):
    n, m = map(int, input().split())

    li_1.append(n)
    li_2.append(m)

check_li = [0] * 1001
for num in li_1:
    check_li[num] += 1

for idx, num in enumerate(check_li):
    if num == 1:
        ans_n += idx
        break

check_li = [0] * 1001
for num in li_2:
    check_li[num] += 1

for idx, num in enumerate(check_li):
    if num == 1:
        ans_m += idx
        break

print(ans_n, ans_m)