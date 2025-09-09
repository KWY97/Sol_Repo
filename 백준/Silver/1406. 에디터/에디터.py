import sys
input = sys.stdin.readline

temp = list(input().rstrip())
n = int(input())
stack = []

for _ in range(n):
    orders = input().split()

    if orders[0] == 'L':
        if temp:
            stack.append(temp.pop())
    elif orders[0] == 'D':
        if stack:
            temp.append(stack.pop())
    elif orders[0] == 'B':
        if temp:
            temp.pop()
    elif orders[0] == 'P':
        temp.append(orders[1])

ans = ''.join(temp) + ''.join(reversed(stack))
print(ans)