word = input()
cnt = 0
for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
print(cnt)