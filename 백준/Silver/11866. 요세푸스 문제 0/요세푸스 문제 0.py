import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
ans = []

for i in range(1, n + 1):
    arr.append(i)

idx = ((k-1) % n)
ans.append(arr[idx])
arr[idx] = 0
cnt = 1

while cnt < n:
    steps_to_move = k
    
    while steps_to_move > 0:
        idx = (idx + 1) % n
        if arr[idx] != 0:
            steps_to_move -= 1
    
    ans.append(arr[idx])
    arr[idx] = 0
    cnt += 1

print("<"  + ", ".join(map(str, ans)) + ">")
