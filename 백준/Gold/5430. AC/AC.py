import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
out = []

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    nums = input().rstrip()

    temp_nums = nums[1:-1]
    if temp_nums:
        dq = deque(temp_nums.split(','))
    else:
        dq = deque()

    rv = False
    ok = True

    for cmd in p:
        if cmd == 'R':
            rv = not rv
        elif cmd == 'D':
            if dq:
                if rv:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                out.append('error')
                ok = False
                break

    if ok:
        if rv:
            dq.reverse()
        out.append('[' + ','.join(dq) + ']')

print('\n'.join(out))