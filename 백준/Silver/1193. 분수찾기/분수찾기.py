def find_line(N):
    current_num = 1
    line = 1

    while True:
        # 현재 줄의 원소의 개수
        num_in_line = line

        # 현재 줄의 가장 마지막 원소
        max_num_in_line = current_num + num_in_line - 1

        if current_num <= N <= max_num_in_line:
            position_in_line = N - current_num + 1
            return line, position_in_line

        current_num = max_num_in_line + 1
        line += 1

N = int(input())
bunja = 1
bunmo = 1

line, position = find_line(N)
ans_li = []

for i in range(1, line + 1):
    if line % 2 != 0:
        ans_li.append(str(line + 1 - i) + '/' + str(i))
    else:
        ans_li.append(str(i) + '/' + str(line + 1 - i))

print(ans_li[position - 1])