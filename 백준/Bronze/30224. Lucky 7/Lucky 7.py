def contain_check(n):
    if '7' in str(n):
        return True
    return False

def division_check(n):
    if n % 7 == 0:
        return True
    return False

N = int(input())
is_contain_seven = contain_check(N)
is_division_seven = division_check(N)

if not is_contain_seven:
    if not is_division_seven:
        print(0)
    else:
        print(1)
else:
    if not is_division_seven:
        print(2)
    else:
        print(3)
