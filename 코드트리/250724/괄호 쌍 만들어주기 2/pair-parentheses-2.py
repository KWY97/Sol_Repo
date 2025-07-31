a = input()

# Please write your code here.
n = len(a)
cnt = 0

for i in range(n-1):
    for j in range(i+1, n-1):
        if a[i] == a[i+1] == '(' and\
            a[j] == a[j+1] == ')':
            cnt += 1

print(cnt)