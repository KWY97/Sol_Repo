for tc in range(1, int(input())+1):
    n = list(map(int, input().split()))
    ans = 0
    for x in n:
        if x % 2 == 0:
            continue
        ans += x
    print(f'#{tc} {ans}')