word = input()
N = len(word)
ans = 1
for i in range(N // 2):
    if word[i] == word[N - 1 - i]:
        continue
    else:
        ans = 0
        break
print(ans)