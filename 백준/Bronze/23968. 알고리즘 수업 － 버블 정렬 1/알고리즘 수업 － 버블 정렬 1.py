import sys
input = sys.stdin.readline

def bubble_sort(array, target_cnt, N):
    n = N
    cnt = 0

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                cnt += 1
                if cnt == target_cnt:
                    return [array[j], array[j+1]]
    return [-1]

N, K = map(int, input().split())
array = list(map(int, input().split()))
ans = bubble_sort(array, K, N)

print(*ans)