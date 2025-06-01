def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            one = s[left + 1:right + 1]
            two = s[left:right]
            if one == one[::-1] or two == two[::-1]:
                return 1
            else:
                return 2
    return 0


N = int(input())
for _ in range(N):
    s = input().strip()
    print(is_palindrome(s))
