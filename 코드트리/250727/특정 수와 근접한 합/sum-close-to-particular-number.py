n, s = map(int, input().split())
numbers = list(map(int, input().split()))
ans = None

hap = sum(numbers)

for i in range(n-1):
    for j in range(i+1, n):
        temp = hap - (numbers[i] + numbers[j])
        diff = abs(s - temp)

        if ans is None or ans > diff:
            ans = diff

print(ans)