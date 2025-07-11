n, m = map(int, input().split())

if m == 1 or m == 2:
    print("NEWBIE!")
else:
    if n >= m:
        print("OLDBIE!")
    else:
        print("TLE!")
