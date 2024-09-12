vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    cnt = 0
    a = input()

    if a == '#': # 입력이 끝난 다는말. while문 종료
        break

    new_a = a.lower() # #이 아니면 문장이 들어오니까 소문자로 바꿔주고

    for i in vowel: # i에는 a, e, i, o, u가 들어감
        for j in new_a: # j에는 입력 받은 문장의 요소 하나하나 씩 들어감
            if i == j:
                cnt += 1

    print(cnt)