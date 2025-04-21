import sys
input = sys.stdin.readline

N = int(input())
my_cards = set(map(int, input().split()))
M = int(input())
check_cards = list(map(int, input().split()))
ans = []

for check_card in check_cards:
    if check_card in my_cards:
        ans.append(1)
    else:
        ans.append(0)

print(' '.join(map(str, ans)))