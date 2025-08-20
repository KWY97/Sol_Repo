T = int(input())

for _ in range(T):
    sol = input()
    cnt = 0
    ans = 0

    for char in sol:
        if char == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)