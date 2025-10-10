# 딕셔너리 풀이
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
B_dic = {}

for b in B:
    B_dic[b] = 1

for a in A:
    if a not in B_dic:
        ans.append(a)

if ans:
    ans.sort()
    print(len(ans))
    print(' '.join(map(str, ans)))
else:
    print(0)


# 투포인터 풀이
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# i, j = 0, 0
# ans = []
#
# A.sort()
# B.sort()
#
# while i < N and j < M:
#     if A[i] < B[j]:
#         ans.append(A[i])
#         i += 1
#     elif A[i] == B[j]:
#         i += 1
#         j += 1
#     else:
#         j += 1
#
# while i < N:
#     ans.append(A[i])
#     i += 1
#
# if ans:
#     print(len(ans))
#     print(' '.join(map(str, ans)))
# else:
#     print(0)