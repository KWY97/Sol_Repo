import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
my_dict = dict()
ans = []

for i in arr:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1


m = int(input())
check = list(map(int, input().split()))

for j in check:
    ans.append(my_dict.get(j, 0))

print(" ".join(map(str, ans)))