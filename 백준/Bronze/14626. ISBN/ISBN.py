n = input()
m = int(n[-1])
ans = 0

for i in range(12):
    if n[i] == '*':
        temp = i
    else:
        if i % 2 == 0:
            ans += int(n[i])
        else:
            ans += int(n[i]) * 3


for j in range(10):
    if temp % 2 == 0:
        ans += j
    else:
        ans += j * 3

    if m == (10 - (ans % 10)) % 10:
        print(j)
        break

    if temp % 2 == 0:
        ans -= j
    else:
        ans -= j * 3
