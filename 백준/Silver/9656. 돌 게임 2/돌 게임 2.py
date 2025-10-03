N = int(input())
# 마지막 돌 가져가면 진다
memo =  {
    1: 'CY',
    2: 'SK',
    3: 'CY'
}

for i in range(4, N+1):
    if memo[i-1] == 'SK' or memo[i-3] == 'SK':
        memo[i] = 'CY'
    else:
        memo[i] = 'SK'

print(memo[N])