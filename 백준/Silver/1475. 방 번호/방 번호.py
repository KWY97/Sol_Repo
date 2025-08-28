n = input()
cnt = [0] * 9

for ch in n:
    d = int(ch)
    if d == 9:
        d = 6
    cnt[d] += 1

cnt[6] = (cnt[6] + 1) // 2
print(max(cnt))