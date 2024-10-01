import sys
input = sys.stdin.readline

A = int(input())
B = int(input())

operators = ['+', '-', '*']

for operator in operators:
    print(eval(f'{A}{operator}{B}'))