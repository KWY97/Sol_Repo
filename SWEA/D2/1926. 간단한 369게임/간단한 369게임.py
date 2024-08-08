N = int(input())

for i in range(1, N + 1):
    i = str(i)
    clap_num = i.count('3') + i.count('6') + i.count('9')
    if clap_num == 0:
        print(i, end = ' ')
    else:
        print(clap_num * '-', end = ' ')