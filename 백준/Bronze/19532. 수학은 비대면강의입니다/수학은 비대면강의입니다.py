import sys
input = sys.stdin.readline


a, b, c, d, e, f = map(int, input().split())

D = (a * e) - (b * d)

x = ((c * e) - (b * f)) / D
y = ((-(c * d)) + (a * f)) / D

print(int(x), int(y))