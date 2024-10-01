import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = list(map(int, input().split()))
D = A * B

for num in C:
    print(num - D, end=' ')