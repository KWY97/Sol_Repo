import sys
input = sys.stdin.readline

temp_balloon = []
ans = []

N = int(input())
nums = list(map(int, input().split()))

for i, num in enumerate(nums):
    temp_balloon.append([num, i + 1])

move = temp_balloon[0][0]
ans.append(temp_balloon[0][1])
balloon = temp_balloon[1:]

idx = 0

while balloon:
    if move > 0:
        idx = (idx + (move - 1)) % len(balloon)
    else:
        idx = (idx + move) % len(balloon)

    pung = balloon.pop(idx) 
    move = pung[0]
    ans.append(pung[1]) 

print(*ans)
