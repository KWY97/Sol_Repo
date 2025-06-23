from itertools import permutations

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]
ans_list = list(permutations(N_list, M))
for ans in ans_list:
    print(' '.join(map(str, ans)))