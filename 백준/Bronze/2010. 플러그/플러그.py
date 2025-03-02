import sys
input = sys.stdin.readline

multitap = int(input())
plug = 0

for _ in range(multitap):
    plug += int(input())

print(plug - (multitap-1))