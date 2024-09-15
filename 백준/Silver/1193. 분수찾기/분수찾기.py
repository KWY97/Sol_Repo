def find_line(N):
    current_num = 1
    line = 1

    while True:
        num_in_line = line

        max_num_in_line = current_num + num_in_line - 1

        if current_num <= N <= max_num_in_line:
            position_in_line = N - current_num + 1
            return line, position_in_line

        current_num = max_num_in_line + 1
        line += 1

N = int(input())

line, position = find_line(N)
ans_li = []

for i in range(1, line + 1):
    if line % 2 != 0:
        ans_li.append(str(line + 1 - i) + '/' + str(i))
    else:
        ans_li.append(str(i) + '/' + str(line + 1 - i))

print(ans_li[position - 1])