s_li = list(input().split())
N = len(s_li)
ans = ''

for i, s in enumerate(s_li):
    n = len(s)
    step = 0

    while step < n:
        if s[step] in ['a', 'e', 'i', 'o', 'u']:
            ans += s[step]
            step += 3
        else:
            ans += s[step]
            step += 1
    if i != N-1:
        ans += ' '

print(ans)