s = input()
n = len(s)
ans = None

for i in range(1, n-1):
    for j in range(i+1, n):
        a = s[:i]
        b = s[i:j]
        c = s[j:]

        r_a = ''.join(list(reversed(a)))
        r_b = ''.join(list(reversed(b)))
        r_c = ''.join(list(reversed(c)))

        new_s = r_a + r_b + r_c

        if ans is None or ans > new_s:
            ans = new_s
print(ans)