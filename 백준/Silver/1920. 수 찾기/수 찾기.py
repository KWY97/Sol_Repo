import sys
input = sys.stdin.readline

N = int(input())
set_1 = set(map(int, input().split()))
M = int(input())
arr_2 = list(map(int, input().split()))

for num in arr_2:
    if num in set_1:
        print(1)
    else:
        print(0)