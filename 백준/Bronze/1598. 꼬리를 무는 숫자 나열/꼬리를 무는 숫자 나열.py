a, b = map(int, input().split())
row_a = -(-a//4)
row_b = -(-b//4)

if a % 4 == 0:
    col_a = 4
else:
    col_a = a % 4

if b % 4 == 0:
    col_b = 4
else:
    col_b = b % 4


ans = abs(row_a - row_b) + abs(col_a - col_b)
print(ans)