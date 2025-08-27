N, M = map(int, input().split())
info_dic = {}

for _ in range(N):
    address, pw = input().split()
    info_dic[address] = pw

for _ in range(M):
    search_address = input()
    print(info_dic[search_address])
