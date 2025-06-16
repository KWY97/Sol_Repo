N = int(input())

i = (N-1, -1, -1)
j = (1, 2*N, 2)

for i in range(1, N+1):
    print(" " * (N-i) + "*" * (2 * i - 1))