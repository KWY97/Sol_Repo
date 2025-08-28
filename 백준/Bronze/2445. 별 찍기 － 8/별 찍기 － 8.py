n = int(input())

for i in range(n):
    print(('*' * (i+1)) + (' ' * (2 * (n - i - 1))) + ('*' * (i+1)))

for j in range(n-1, 0, -1):
    print(('*' * j) + (' ' * ((n - j) * 2)) + ('*' * j))