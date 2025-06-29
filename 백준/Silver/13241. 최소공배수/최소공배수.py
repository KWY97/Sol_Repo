def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

n, m = map(int, input().split())

my_gcd = gcd(n, m)

print((n * m) // my_gcd)