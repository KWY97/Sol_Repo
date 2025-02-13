N, K = map(int, input().split())
scores = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        if scores[i] < scores[j]:
            scores[i], scores[j] = scores[j], scores[i]

print(scores[K-1])