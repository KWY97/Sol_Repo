N = int(input())
my_li = []

for _ in range(N):
    my_li.append(input())

for i in range(N):
    print(f'{i+1}. {my_li[i]}')