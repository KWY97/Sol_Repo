import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pocketmons = [input().strip() for _ in range(n)]
problem = [input().strip() for _ in range(m)]
ans = []

for x in problem:
    if x.isalpha() == False:
        target_idx = (int(x)-1)
        ans.append(pocketmons[target_idx])
    else:
        target_name = x
        ans.append((pocketmons.index(target_name))+1)

print("\n".join(map(str, ans)))