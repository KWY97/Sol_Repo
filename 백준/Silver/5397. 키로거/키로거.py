T = int(input())

for _ in range(T):
    in_string = list(input())
    key_first = []
    key_second = []

    for c in in_string:
        if c == '<':
            if key_first:
                key_second.append(key_first.pop())
        elif c == '>':
            if key_second:
                key_first.append(key_second.pop())
        elif c == '-':
            if key_first:
                key_first.pop()
        else:
            key_first.append(c)
    print(''.join(key_first) + ''.join(reversed(key_second)))