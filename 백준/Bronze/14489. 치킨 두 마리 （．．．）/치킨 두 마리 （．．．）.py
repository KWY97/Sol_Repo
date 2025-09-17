A, B = map(int, input().split())
chicken = int(input())

cost = A + B
two_chicken = 2 * chicken

if cost >= two_chicken:
    print(cost - two_chicken)
else:
    print(cost)