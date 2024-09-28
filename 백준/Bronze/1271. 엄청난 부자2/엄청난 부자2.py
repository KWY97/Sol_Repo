import sys
input = sys.stdin.readline

money, people = map(int, input().split())
per_money = money // people
changes = money % people
print(per_money)
print(changes)