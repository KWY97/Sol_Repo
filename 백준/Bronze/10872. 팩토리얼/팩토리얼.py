def fac(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * fac(num-1)

N = int(input())
print(fac(N))
