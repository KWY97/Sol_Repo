T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apt = [[] for _ in range(k+1)]

    for i in range(k+1):
        for j in range(n):
            if i == 0:
                apt[i].append(j+1)
            else:
                if j == 0:
                    apt[i].append(1)
                else:
                    temp = apt[i-1][j] + apt[i][j-1]
                    apt[i].append(temp)

    print(apt[k][n-1])