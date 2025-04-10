n = int(input())
li = [0, 1, 2, 3]
for _ in range(n):
    a, b = map(int, input().split())
    for idx, num in enumerate(li):
        if num == a:
            c = idx
        if num == b:
            d = idx
    li[c], li[d] = li[d], li[c]
print(li[1])