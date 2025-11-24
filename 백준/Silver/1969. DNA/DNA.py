N, M = map(int, input().split())
s = [{} for _ in range(M)]
ans1 = ""
ans2 = 0

for _ in range(N):
    DNA = input()

    for i in range(M):
        if DNA[i] in s[i]:
            s[i][DNA[i]] += 1
        else:
            s[i][DNA[i]] = 1

for i in range(M):
    items = sorted(s[i].items(), key=lambda x: (-x[1], x[0]))
    best_char = items[0][0]
    ans1 += best_char

    for j in range(1, len(items)):
        ans2 += items[j][1]

print(ans1)
print(ans2)