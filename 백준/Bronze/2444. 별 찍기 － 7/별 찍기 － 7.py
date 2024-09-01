N = int(input())
for i in range(1, N+1):
    print((" " * (N - i)) + "*" * (i*2 - 1))
for j in range(1, N):
    print((" " * j) + "*" * ((N-j)*2 - 1))