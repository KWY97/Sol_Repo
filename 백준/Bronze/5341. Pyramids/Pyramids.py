while True:
    n = int(input())
    sum = 0

    if n == 0:
        break

    for i in range(1, n+1):
        sum += i

    print(sum)