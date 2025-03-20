jinho = input()
n = int(input())
friends = []
cnt = 0
for _ in range(n):
    friends.append(input())

for friend in friends:
    if jinho == friend:
        cnt += 1

print(cnt)