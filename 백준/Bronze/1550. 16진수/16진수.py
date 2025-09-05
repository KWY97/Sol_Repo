s = input()
n = len(s)
l = [0] * n
ans = 0

for i in range(n):
    if s[i].isdecimal():
        l[i] = int(s[i])
    else:
        l[i] = ord(s[i]) - 55

for j in range(n):
    ans += l[j] * (16 ** (n-j-1))

print(ans)
