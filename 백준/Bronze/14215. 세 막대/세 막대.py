arr = []

a, b, c = map(int, input().split())

arr.append(a)
arr.append(b)
arr.append(c)

max_line = max(arr)
arr.remove(max_line)

line_1, line_2 = arr[0], arr[1]

if max_line < line_1 + line_2:
    print(max_line + line_1 + line_2)
else:
    max_line = line_1 + line_2 - 1
    print(max_line + line_1 + line_2)