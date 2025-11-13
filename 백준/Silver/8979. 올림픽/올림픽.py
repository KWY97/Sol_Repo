# 국가의 수, 등수를 알고 싶은 국가
N, K = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

# 순위 정렬
countries.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

# K번째 국가의 인덱스 찾기
for i, country in enumerate(countries):
    if country[0] == K:
        idx = i
        break

# 등수 찾기
for i in range(N):
    if countries[i][1:] == countries[idx][1:]:
        print(i+1)
        break