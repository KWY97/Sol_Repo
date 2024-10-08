def f():
    temp = []
    for v in range(M, 0, -1):
        temp.append(v)
        if len(temp) == N:
            return temp

def fac(n):
    temp_num = 1
    for i in range(1, n+1):
        temp_num *= i
    return temp_num

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    num = 1
    my_li = f()
    for v in my_li:
        num *= v
    print(num//fac(N))