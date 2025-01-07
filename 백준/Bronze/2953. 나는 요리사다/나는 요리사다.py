scores = [list(map(int, input().split())) for _ in range(5)]

max_score = 0
max_person = 0

for index, score in enumerate(scores):
    if max_score < sum(score):
        max_score = sum(score)
        max_person = index + 1
print(max_person, max_score)
