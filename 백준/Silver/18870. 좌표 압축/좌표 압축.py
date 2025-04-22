import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
set_arr = sorted(set(arr))

my_dict = {}
ans = []

for i in range(len(set_arr)):
    my_dict[set_arr[i]] = i

for i in range(len(arr)):
    num = arr[i]
    ans.append(my_dict[num])

print(" ".join(map(str, ans)))