N = int(input())
infos = [input() for _ in range(N)]
check = {}
cnt = 0

# ENTER를 기준으로 처음 나오는 닉네임을 카운트하기
for info in infos:
    if info == "ENTER":
        check = {}
    else:
        if info not in check:
            check[info] = 1
            cnt += 1

print(cnt)