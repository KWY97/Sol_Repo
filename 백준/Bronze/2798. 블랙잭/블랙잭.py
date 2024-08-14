N, M = map(int, input().split())
cards = list(map(int, input().split()))
pick = 3 # 뽑아야 되는 카드 3장
ans_list = []

for i in range(N - pick + 1):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum = 0 # 마지막 고를 때 마다 초기화
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                ans_list.append(sum)

print(max(ans_list))