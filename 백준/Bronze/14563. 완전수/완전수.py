def f(num):
    ans = []

    for i in range(1, num):
        if num % i == 0:
            ans.append(i)

    if sum(ans) == num:
        return "Perfect"
    elif sum(ans) < num:
        return "Deficient"
    else:
        return "Abundant"

t = int(input())
li = list(map(int, input().split()))

for n in li:
    print(f(n))