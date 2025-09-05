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
    # 0은 덧셈, 1은 곱셈
    for i in range(n):
        if s[i] == '(':
            if stack:
                stack.append(['(', 0, temp])
            else:
                stack.append(['(', 1, temp])
            temp = None
        elif s[i] == '[':
            if stack:
                stack.append(['[', 0, temp])
            else:
                stack.append(['[', 1, temp])
            temp = None
        elif s[i] == ')':
            shape, cal, prev_temp = stack.pop()
            # 값 계산
            # 처음 계산 되는 것이라면
            if temp is None:
                frame_value = 2
            else:
                frame_value = temp * 2

            if prev_temp is None:
                temp = frame_value
            else:
                temp = prev_temp + frame_value

            # 곱셈 이라면
            if cal:
                ans += temp
                temp = None

        elif s[i] == ']':
            shape, cal, prev_temp = stack.pop()
            # 값 계산
            # 처음 계산 되는 것이라면
            if temp is None:
                frame_value = 3
            else:
                frame_value = temp * 3

            if prev_temp is None:
                temp = frame_value
            else:
                temp = prev_temp + frame_value

            # 곱셈 이라면
            if cal:
                ans += temp
                temp = None

    print(ans)