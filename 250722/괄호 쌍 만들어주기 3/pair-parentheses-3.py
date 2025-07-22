A = input()

# Please write your code here.
N = len(A)
cnt = 0

for i in range(N):
    if A[i] == '(':
        for j in range(i+1, N):
            if A[j] == ')':
                cnt += 1

print(cnt)