N, M = map(int, input().split())
singers = {}

for _ in range(N):
    name_singer = input()
    singers[name_singer] = []
    num_member = int(input())

    for _ in range(num_member):
        name_member = input()
        singers[name_singer].append(name_member)

for _ in range(M):
    question = input()
    type_question = int(input())

    if type_question == 0:
        sorted_singers = sorted(singers[question])
        for singer in sorted_singers:
            print(singer)
    else:
        for key in singers:
            if question in singers[key]:
                print(key)
                break