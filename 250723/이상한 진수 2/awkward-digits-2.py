a = int(input())
n = len(str(a))
max_num_bi = 0

for i in range(n):
    if (str(a))[i] == '1':
        temp = a - 10**(n-1-i)
    elif (str(a))[i] == '0':
        temp = a + 10**(n-1-i)

    if max_num_bi < temp:
        max_num_bi = temp

l = len(str(max_num_bi))
ans = 0

for i in range(l-1, -1, -1):
    ans += int((str(max_num_bi))[i]) * 2**(l-1-i)

print(ans)