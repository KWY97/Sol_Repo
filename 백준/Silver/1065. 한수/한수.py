def hansu(n):
    if 1 <= n <= 99:
        return 1
    elif len(str(n)) == 3:
        if int(str(n)[1]) - int(str(n)[0]) == int(str(n)[2]) - int(str(n)[1]):
            return 1
        else:
            return 0
    else:
        return 0

N = int(input())
cnt = 0
for i in range(1, N+1):
    cnt += hansu(i)
print(cnt)