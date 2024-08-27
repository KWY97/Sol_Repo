T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    for v in S:
        print(R*v, end = "")
    print()