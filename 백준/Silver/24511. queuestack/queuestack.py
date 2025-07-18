from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
D = deque()

for i in range(N):
    if A[i] == 0:
        D.append(B[i])

for j in range(M):
    D.appendleft(C[j])
    print(D.pop(), end=' ')

