def hanoi(n, start, temp, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, end, temp)
    print(start, end)
    hanoi(n-1, temp, start, end)

N = int(input())
print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)
