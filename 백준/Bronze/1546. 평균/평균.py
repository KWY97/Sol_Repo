N = int(input()) # 과목의 개수
scores = list(map(int, input().split())) # 시험 점수
new_scores = 0

max_score = max(scores)

for score in scores:
    new_scores += (score/max_score * 100)

ans = new_scores/N

print(ans)