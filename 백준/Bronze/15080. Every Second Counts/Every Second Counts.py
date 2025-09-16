s_time = list(map(int, input().split(' : ')))
e_time = list(map(int, input().split(' : ')))

s = s_time[0] * 3600 + s_time[1] * 60 + s_time[2]
e = e_time[0] * 3600 + e_time[1] * 60 + e_time[2]

if s <= e:
    print(e-s)
else:
    print(((24 * 3600) + e) - s)