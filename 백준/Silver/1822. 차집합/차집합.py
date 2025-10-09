N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
B_dic = {}

for b in B:
    B_dic[b] = 1

for a in A:
    if a not in B_dic:
        ans.append(a)

if ans:
    ans.sort()
    print(len(ans))
    print(' '.join(map(str, ans)))
else:
    print(0)
