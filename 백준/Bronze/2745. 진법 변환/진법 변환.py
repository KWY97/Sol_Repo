N, B = input().split()
N = N[::-1]
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

for i in range(len(N)):
    for j in range(len(num)):
        if N[i] == num[j]:
            sum += j * (int(B)**i)
            break
print(sum)