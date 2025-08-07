a = input()
b = input()

a_dic = {}
b_dic = {}

cnt = 0

for char in a:
    a_dic[char] = a_dic.get(char, 0) + 1

for char in b:
    b_dic[char] = b_dic.get(char, 0) + 1

for char in a_dic:
    if char not in b_dic:
        cnt += a_dic[char]
    else:
        if a_dic[char] != b_dic[char]:
            cnt += abs(a_dic[char] - b_dic[char])

for char in b_dic:
    if char not in a_dic:
        cnt += b_dic[char]

print(cnt)