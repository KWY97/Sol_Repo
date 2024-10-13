N = int(input())
words = [input() for _ in range(N)]

words = list(set(words))
M = len(words)

words.sort()

for i in range(M - 1, 0, -1):
    for j in range(i):
        if len(words[j]) > len(words[j+1]):
            words[j], words[j+1] = words[j+1], words[j]

for word in words:
    print(word)