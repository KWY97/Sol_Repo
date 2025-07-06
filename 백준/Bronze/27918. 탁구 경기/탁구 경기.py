n = int(input())
d_count = 0
p_count = 0

for _ in range(n):
    s = input()
    if s == "D":
        d_count += 1
    else:
        p_count += 1
    
    if abs(d_count - p_count) == 2:
        break

print(f'{d_count}:{p_count}')