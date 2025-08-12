def f(s, left, right):
    global cnt

    if left >= right:
        return [1, cnt]
    elif s[left] != s[right]:
        return [0, cnt]
    else:
        cnt += 1
        return f(s, left+1, right-1)

T = int(input())

for _ in range(T):
    in_string = input()
    n = len(in_string)
    cnt = 1
    print(*(f(in_string, 0, n-1)))