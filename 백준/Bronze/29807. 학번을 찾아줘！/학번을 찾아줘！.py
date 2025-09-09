n = int(input())
in_scores = list(map(int, input().split()))

k, m, e, r, e2 = 0, 1, 2, 3, 4
scores = [0] * 5

for i in range(n):
    scores[i] = in_scores[i]

score1 = abs(scores[k] - scores[e])
score2 = abs(scores[m] - scores[r])
score3 = scores[e2] * 707

if scores[k] > scores[e]:
    score1 *= 508
else:
    score1 *= 108

if scores[m] > scores[r]:
    score2 *= 212
else:
    score2 *= 305

print((score1 + score2 + score3) * 4763)