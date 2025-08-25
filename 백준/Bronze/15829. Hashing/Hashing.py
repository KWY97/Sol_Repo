L = int(input())
s = input()
M = 1234567891
r = 31
ans = 0

for i in range(L):
    ans += (ord(s[i]) - 96) * (r ** i)
print(ans % M)