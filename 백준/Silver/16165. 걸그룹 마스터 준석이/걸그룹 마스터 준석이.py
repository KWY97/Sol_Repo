N, M = map(int, input().split())
group2signer_dict = {}
singer2group_dict = {}

for _ in range(N):
    group = input()
    group2signer_dict.setdefault(group, [])

    K = int(input())

    for _ in range(K):
        singer = input()
        group2signer_dict[group].append(singer)
        singer2group_dict[singer] = group

for _ in range(M):
    q_name = input()
    q_num = int(input())

    if q_num:
        print(singer2group_dict[q_name])
    else:
        sorted_singer = sorted(group2signer_dict[q_name])

        for singer in sorted_singer:
            print(singer)
