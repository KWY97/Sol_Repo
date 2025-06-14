import sys
input = sys.stdin.readline

def gcd(n, m):
    while m > 0:
        temp = n % m
        n = m
        m = temp
    return n

N = int(input())
a_numbers = list(map(int, input().split()))
M = int(input())
b_numbers = list(map(int, input().split()))
A = 1
B = 1

for num in a_numbers:
    A *= num

for num in b_numbers:
    B *= num

ans = str(gcd(A, B))
l = len(ans)

if l > 9:
    ans = ans[-9:]
print(ans)
