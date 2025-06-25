from itertools import combinations

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]
results = list(combinations(N_list, M))
for result in results:
    print(' '.join(map(str, result)))