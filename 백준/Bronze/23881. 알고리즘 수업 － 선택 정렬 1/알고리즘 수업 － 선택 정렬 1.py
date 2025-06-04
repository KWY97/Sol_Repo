import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))


def selection_sort(array, n, k):
    count = 0
    for i in range(n-1, 0, -1):
        max_index = i
        for j in range(i+1):
            if array[max_index] < array[j]:
                max_index = j

        if max_index != i:
            array[max_index], array[i] = array[i], array[max_index]
            count += 1
            if count == k:
                return [array[max_index], array[i]]
    return [-1]


ans = selection_sort(arr, N, K)
print(*ans)