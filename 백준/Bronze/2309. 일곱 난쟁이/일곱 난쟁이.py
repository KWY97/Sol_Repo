import sys
input = sys.stdin.readline

li = []
for _ in range(9):
    li.append(int(input()))

li.sort()
my_sum = sum(li)

for i in range(9):
    for j in range(i+1, 9):
        if my_sum - li[i] - li[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(li[k])
            exit()