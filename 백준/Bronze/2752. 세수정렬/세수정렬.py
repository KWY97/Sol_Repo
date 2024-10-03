import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
li = [a, b, c]
li.sort()
print(*li)