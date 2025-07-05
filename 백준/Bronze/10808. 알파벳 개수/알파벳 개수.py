alphabets = dict()

for i in range(97, 123):
    alphabets[chr(i)] = 0

s = input()
for c in s:
    alphabets[c] += 1

ans = list(alphabets.values())
print(' '.join(map(str, ans)))