def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if (n1 < 0 < n2) or (n1 > 0 > n2):
            return -(abs(n1) // abs(n2))
        else:
            return n1 // n2

question = list(input().split())

num1 = int(question[0])
num2 = int(question[2])
num3 = int(question[4])

op1 = question[1]
op2 = question[3]

ans1 = cal(cal(num1, num2, op1), num3, op2)
ans2 = cal(num1, cal(num2, num3, op2), op1)

ans = [ans1, ans2]
ans.sort()

for a in ans:
    print(a)