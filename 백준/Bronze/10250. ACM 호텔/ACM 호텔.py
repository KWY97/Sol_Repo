T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H != 0:
        room = (N // H) + 1
        height = N % H
    else:
        room = (N // H)
        height = H


    if room < 10:
        room = '0' + str(room)
    else:
        room = str(room)

    print(str(height) + room)