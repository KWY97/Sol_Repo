T = int(input())

for _ in range(T):
    clothes = {}
    n = int(input())
    total = 1
    for _ in range(n):
        c_name, c_type = input().split()
        clothes.setdefault(c_type, []).append(c_name)

    for k in clothes:
        total *= (len(clothes[k]) + 1)

    print(total-1)