n = int(input())
for _ in range(n):
    m = int(input())
    numbers = list(map(int, input().split()))
    print(f'{min(numbers)} {max(numbers)}')