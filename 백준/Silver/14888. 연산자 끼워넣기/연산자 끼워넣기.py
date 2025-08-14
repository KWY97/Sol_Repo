import sys
input = sys.stdin.readline

def backtrack():
    if len(path) == total_len:
        operator_result.append(path[:])
        return

    i = 0
    while i < 4:  # 기호 종류 개수
        if operator_counts[i] > 0:
            operator_counts[i] -= 1
            path.append(symbols[i])
            backtrack()
            path.pop()
            operator_counts[i] += 1
        i += 1

N = int(input())
numbers = list(map(int, input().split()))
operator_counts = list(map(int, input().split()))
symbols = ['+', '-', '*', '/']
total_len = N-1
operator_result = []
path = []

backtrack()
MAX = None
MIN = None

total_li = [0] * (N + total_len)
m = len(total_li)
for i in range(0, m, 2):
    total_li[i] = numbers[i//2]

for operator in operator_result:
    total_li[1] = operator[0]
    for j in range(3, m, 2):
        total_li[j] = operator[j//2]


    point_num = total_li[0]
    i = 1

    while i < m:
        op = total_li[i]
        num = total_li[i+1]

        if op == '+':
            point_num = point_num + num
        elif op == '-':
            point_num = point_num - num
        elif op == '*':
            point_num = point_num * num
        elif op == '/':
            point_num = int(point_num / num)
        i += 2

    if MAX is None or MAX < point_num:
        MAX = point_num
    if MIN is None or MIN > point_num:
        MIN = point_num
print(MAX)
print(MIN)