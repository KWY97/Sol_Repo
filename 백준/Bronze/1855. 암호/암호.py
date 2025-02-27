K = int(input())
N = list(input())
arr = []
ans_arr = []

for i in range(0, len(N), K):
    arr.append(N[i:i+K])

for j in range(len(arr)):
    if j % 2 == 0:
        ans_arr.append(arr[j])
    else:
        temp = []
        for k in range(K-1, -1, -1):
            temp.append(arr[j][k])
        ans_arr.append(temp)

for i in range(K):
    for j in range(len(ans_arr)):
        print(ans_arr[j][i], end='')
