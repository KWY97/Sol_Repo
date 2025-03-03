N = int(input())
arr = list(map(int, input().split()))
temp = []
flag = 0

target = 1

for num in arr:
    if num == target:
        target += 1
        while (len(temp) != 0) and temp[-1] == target:
            temp.pop()
            target += 1
    else:
        if (len(temp) > 1) and (temp[-2] < temp[-1]):
            print('Sad')
            flag = 1
            break
        temp.append(num)

if flag == 0:
    print('Nice')