checks = []
eng = {}
for i in range(65, 91):
    eng[chr(i)] = 0

max_cnt = 0

word = input().upper()

for alphabet in word:
    eng[alphabet] += 1

for cnt in eng.values():
    if max_cnt < cnt:
        max_cnt = cnt

for k, v in eng.items():
    if v == max_cnt:
        checks.append([k, v])

if len(checks) == 1:
    print(checks[0][0])
else:
    print('?')