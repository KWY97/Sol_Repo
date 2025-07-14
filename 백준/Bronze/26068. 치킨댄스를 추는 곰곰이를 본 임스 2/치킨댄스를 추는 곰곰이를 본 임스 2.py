T = int(input())
cnt = 0
for _ in range(T):
    i = input()
    if int(i[2:]) <= 90:
        cnt += 1
print(cnt)