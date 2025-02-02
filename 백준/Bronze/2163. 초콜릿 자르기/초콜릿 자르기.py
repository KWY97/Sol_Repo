import sys
input = sys.stdin.readline
N, M = map(int, input().split())
print((M * (N - 1)) + (M - 1))