import itertools

n = int(input())
k = int(input())

cards = []
for _ in range(n):
    card = int(input())
    cards.append(card)

result = set()

for i in itertools.permutations(cards, k):
    result.add(''.join(map(str, i)))

print(len(result))