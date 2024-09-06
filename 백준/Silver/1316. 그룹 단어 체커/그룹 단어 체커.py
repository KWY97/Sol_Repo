def my_func(word):
    check = []
    cnt = 0
    for i in range(M):
        if word[i] in check:
            if word[i-1] == word[i]:
                continue
            else:
                return 0
        else:
            check.append(word[i])
    cnt += 1
    return cnt

N = int(input())
sum = 0
for _ in range(N):
    word = input()
    M = len(word)
    sum += my_func(word)
print(sum)