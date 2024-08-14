def male(switch, s_num): # switch: 스위치 상태, s_num: 스위치 번호
    s_num_list = []

    # 동작 시킬 수 있는 스위치를 구하는 과정
    for i in range(1, cnt_switch + 1):
        if i % s_num == 0: # 배수라면
            s_num_list.append(i)

    for x in s_num_list:
        if switch[x-1] == 0:
            switch[x-1] = 1
        else:
            switch[x-1] = 0
    return switch

def female(switch, s_num):
    s_num -= 1  # 인덱스 조정
    left = s_num
    right = s_num

    # 좌우 대칭으로 스위치 상태를 반전시킬 수 있는 최대 범위를 찾습니다.
    while left >= 0 and right < len(switch) and switch[left] == switch[right]:
        left -= 1
        right += 1

    # 마지막 대칭 부분의 범위
    for i in range(left + 1, right):
        switch[i] = 1 - switch[i]  # 0을 1로, 1을 0으로 변경
    return switch

cnt_switch = int(input()) # 스위치 개수 입력
state_switch = list(map(int, input().split())) # 스위치의 상태 입력
cnt_student = int(input()) # 학생 수 입력
user_info = [] # 각 학생의 성별과 스위치번호를 받을 리스트


for _ in range(cnt_student):
    gender, num_switch = map(int, input().split())
    user_info.append([gender, num_switch])


for i in range(cnt_student): #len(user_info) == cnt_student
    if user_info[i][0] == 1:
        ans = male(state_switch, user_info[i][1])
    else:
        ans = female(state_switch, user_info[i][1])

for i in range(cnt_switch):
    print(ans[i], end = ' ')
    if (i+1) % 20 == 0:
        print()