tc = int(input())
ans = []

for _ in range(tc):
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    print(numbers[2])