def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    my_gcd = gcd(a, b)
    return a * b // my_gcd

N, M = map(int, input().split())
print(gcd(N, M))
print(lcm(N, M))