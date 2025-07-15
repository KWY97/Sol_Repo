def check(s):
    stack = []

    for c in s:
        if c == "(":
            stack.append(")")
        elif not stack:
            return "NO"
        elif stack:
            stack.pop()

    if not stack:
        return "YES"
    else:
        return "NO"


T = int(input())

for _ in range(T):
    s = input()

    print(check(s))