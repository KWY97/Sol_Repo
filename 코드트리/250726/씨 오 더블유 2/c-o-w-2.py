n = int(input())
s = input()
ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if s[i] == 'C' and s[j] == 'O' and s[k] == 'W':
                ans += 1

print(ans)