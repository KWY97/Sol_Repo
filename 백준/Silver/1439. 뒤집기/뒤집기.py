def count_num(string):
    count_change_to_zero = 0
    count_change_to_one = 0

    if string[0] == '1':
        count_change_to_zero += 1
    else:
        count_change_to_one += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i+1] == '1':
                count_change_to_zero += 1
            else:
                count_change_to_one += 1

    return min(count_change_to_zero, count_change_to_one)

S = input()
print(count_num(S))

