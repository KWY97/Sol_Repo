import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

pocketmon_name_to_num = {}
pocketmon_num_to_name = {}

for i in range(1, n + 1):
    pocketmon_name = input().strip()
    pocketmon_name_to_num[pocketmon_name] = i
    pocketmon_num_to_name[i] = pocketmon_name

for _ in range(m):
    problem = input().strip()
    if problem.isalpha():
        ans.append(pocketmon_name_to_num[problem])
    else:
        ans.append(pocketmon_num_to_name[int(problem)])

print("\n".join(map(str, ans)))