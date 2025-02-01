A = int(input())
B = int(input())
C = int(input())

ans = str(A * B * C)
my_list = [0] * 10

for num in ans:
    my_list[int(num)] += 1

for num_cnt in my_list:
    print(num_cnt)