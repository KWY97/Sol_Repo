import sys

S, E, Q = input().split()
attendance = set()
enter = {}
exit = {}

while True:
    line = sys.stdin.readline().strip()

    if not line:
        break

    time, name = line.split()

    if time <= S:
        enter[name] = True
    elif E <= time <= Q:
        exit[name] = True

    attendance.add(name)

cnt = 0
for name in attendance:
    if name in enter and name in exit:
        cnt += 1

print(cnt)