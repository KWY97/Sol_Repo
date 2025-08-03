import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words_dict = {}

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue

    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1


words = list(words_dict.items())
words.sort(key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))

for word in words:
    print(word[0])