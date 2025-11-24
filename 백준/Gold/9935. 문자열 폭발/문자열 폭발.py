s = input()
target = input()
stack = []
t = len(target)

for c in s:
    stack.append(c)
    l = len(stack)

    if l >= t:
        comp_s = ''.join(stack[-t:])
        if comp_s == target:
            for _ in range(t):
                stack.pop()

print(''.join(stack) if stack else "FRULA")