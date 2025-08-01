N = int(input())
cnt = 0
check = {'ChongChong': 1}

for _ in range(N):
    p1, p2 = input().split()

    if p1 in check and p2 not in check:
        check[p2] = 1
    elif p2 in check and p1 not in check:
        check[p1] = 1

print(len(check))
