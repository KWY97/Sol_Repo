def check(number):
    length = len(number)

    if length == 1:
        return 'yes'
    elif length == 2:
        if number[0] == number[1]:
            return 'yes'
        else:
            return 'no'
    elif length == 3:
        if number[0] == number[2]:
            return 'yes'
        else:
            return 'no'
    else:
        new_length = (length // 2)
        for i in range(new_length):
            if number[i] == number[(length-1) - i]:
                continue
            else:
                return 'no'
        return 'yes'


while True:
    number = input()

    if number == '0':
        break

    print(check(number))