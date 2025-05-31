import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))
B, C = map(int, input().split())

my_sum = 0

for i in range(N):
    student = n_list[i]

    student -= B
    my_sum += 1

    if student > 0:
        my_sum += -(-student // C)

print(my_sum)