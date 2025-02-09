while True:
    number = input()

    if number == "0":
        break

    a = 2
    b = len(number) - 1
    c = 0

    for num in number:
        if num == "0":
            c += 4
        elif num == "1":
            c += 2
        else:
            c += 3
    
    print(a + b + c)