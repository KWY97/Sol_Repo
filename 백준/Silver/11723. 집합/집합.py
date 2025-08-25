import sys
input = sys.stdin.readline

M = int(input())
s = set()

for _ in range(M):
    order = list(input().split())

    if order[0] == 'add':
        s.add(int(order[1]))
    elif order[0] == 'remove':
        s.discard(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in s:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in s:
            s.remove(int(order[1]))
        else:
            s.add(int(order[1]))
    elif order[0] == 'all':
        for i in range(1, 21):
            s.add(i)
    elif order[0] == 'empty':
        s.clear()