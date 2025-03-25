import sys
input = sys.stdin.readline
N = int(input())

print(round(((N) * (N-1) * (N-2) * (N-3)) / 24))