a = []

for _ in range(3):
    a.append(input())

for i in range(2):
    if a[i] == "black": a[i] = 0
    elif a[i] == "brown": a[i] = 1
    elif a[i] == "red": a[i] = 2
    elif a[i] == "orange": a[i] = 3
    elif a[i] == "yellow": a[i] = 4
    elif a[i] == "green": a[i] = 5
    elif a[i] == "blue": a[i] = 6
    elif a[i] == "violet": a[i] = 7
    elif a[i] == "grey": a[i] = 8
    elif a[i] == "white": a[i] = 9


if a[2] == "black": a[2] = 1
elif a[2] == "brown": a[2] = 10
elif a[2] == "red": a[2] = 100
elif a[2] == "orange": a[2] = 1000
elif a[2] == "yellow": a[2] = 10000
elif a[2] == "green": a[2] = 100000
elif a[2] == "blue": a[2] = 1000000
elif a[2] == "violet": a[2] = 10000000
elif a[2] == "grey": a[2] = 100000000
elif a[2] == "white": a[2] = 1000000000

sum = (a[0] * a[2] * 10) + (a[1] * a[2])


print(sum)