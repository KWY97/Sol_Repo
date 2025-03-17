import sys
input = sys.stdin.readline

scores = []
sum = 0
problem = []

for i in range(8):
    scores.append([int(input()), i+1])

scores.sort(reverse=True)
for i in range(5):
    sum += scores[i][0]
    problem.append(scores[i][1])

problem.sort()
ans = problem

print(sum)
print(*ans)