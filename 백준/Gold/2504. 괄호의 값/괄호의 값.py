def check_right_parentheses():
    f_stack = []

    for i in range(n):
        if s[i] == '(':
            f_stack.append('(')
        elif s[i] == '[':
            f_stack.append('[')
        elif s[i] == ')':
            if not f_stack:
                return 0
            temp2 = f_stack.pop()
            if temp2 == '[':
                return 0
        elif s[i] == ']':
            if not f_stack:
                return 0
            temp2 = f_stack.pop()
            if temp2 == '(':
                return 0

    if f_stack:
        return 0
    return 1

s = input()
n = len(s)
stack = []
ans = 0
temp = None

if not check_right_parentheses():
    print(0)
else:
    # 1은 곱셈, 0은 덧셈
    for i in range(n):
        if s[i] == '(':
            if stack:
                stack.append([1, temp])
            else:
                stack.append([0, temp])
            temp = None
        elif s[i] == '[':
            if stack:
                stack.append([1, temp])
            else:
                stack.append([0, temp])
            temp = None
        elif s[i] == ')':
            cal, prev_temp = stack.pop()

            if temp is None:
                frame_value = 2
            else:
                frame_value = temp * 2

            if prev_temp is None:
                temp = frame_value
            else:
                temp = prev_temp + frame_value

            if not cal:
                ans += temp
                temp = None
        elif s[i] == ']':
            cal, prev_temp = stack.pop()

            if temp is None:
                frame_value = 3
            else:
                frame_value = temp * 3

            if prev_temp is None:
                temp = frame_value
            else:
                temp = prev_temp + frame_value

            if not cal:
                ans += temp
                temp = None
    print(ans)