import sys
input = sys.stdin.readline

def time_to_minute(t):
    '''
    시간 -> 분 전환함수
    :param t: "02:30" (str)
    :return: "150" (int)
    '''

    time, minute = map(int, t.split(':'))
    total_minute = time * 60 + minute

    return total_minute

S, E, Q = input().split()
attendance = {}
filtered = {}
cnt = 0

start = time_to_minute(S)
end = time_to_minute(E)
final_end = time_to_minute(Q)

# 입퇴실 기록 출석부 만들기
while True:
    try:
        T, name = input().split()
        attendance.setdefault(name, []).append(T)
    except:
        break

# 입퇴실 기록 체크
for student, logs in attendance.items():
    has_enter = False
    has_exit = False

    i = 0
    while i < len(logs):
        t = time_to_minute(logs[i])

        if not has_enter and start >= t:
            has_enter = True
        if not has_exit and end <= t <= final_end:
            has_exit = True

        if has_enter and has_exit:
            cnt += 1
            break

        i += 1

print(cnt)
