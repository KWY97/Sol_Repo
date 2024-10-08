def checking(li):
    flag = 1
    for i in range(len(li) - 1):
        if li[i] == li[i+1]:
            continue
        else:
            flag = 2
    return flag

N = int(input())
f_list = []
ans = []

for _ in range(N):
    f_name = input()
    f_list.append(f_name)

length = len(f_name)

for i in range(length):
    check = []
    for j in range(N):
        check.append(f_list[j][i])
    if checking(check) == 1:
        ans.append(check[0])
    else:
        ans.append('?')
print("".join(ans))