def strfly(a, b):
    if len(a) != len(b):
        return "Impossible"
    else:
        my_dict = {}
        for c in a:
            my_dict[c] = my_dict.get(c, 0) + 1

        for k, v in my_dict.items():
            if k not in b:
                return "Impossible"
            else:
                if v != b.count(k):
                    return "Impossible"
    return "Possible"



n = int(input())

for _ in range(n):
    s1, s2 = input().split()
    print(strfly(s1, s2))


