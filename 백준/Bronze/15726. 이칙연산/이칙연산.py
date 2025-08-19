a, b, c = map(int, input().split())

o1 = int(a * (b / c))
o2 = int((a / b) * c)

print(max(o1, o2))