eng = []
check = []
for i in range(97, 123):
    eng.append(chr(i))

ans = [-1 for _ in range(26)]

s = list(input())

for idx, v in enumerate(s):
    if v not in check:
        if v in eng:
            i = eng.index(v)
            ans[i] = idx
            check.append(v)

print(*ans)