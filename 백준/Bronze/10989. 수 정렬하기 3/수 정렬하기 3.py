n = int(input())
numbers = [0] * 10001

for _ in range(n):
    number = int(input())
    numbers[number] += 1
    
for i in range(1, 10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)