T = int(input())

if T == 5:
    k, m, e, r, e2 = map(int, input().split())
    score1 = abs(k-e)
    score2 = abs(m-r)
    score3 = e2 * 707

    if k > e:
        score1 *= 508
    else:
        score1 *= 108

    if m > r:
        score2 *= 212
    else:
        score2 *= 305

    print((score1 + score2 + score3) * 4763)

elif T == 4:
    k, m, e, r = map(int, input().split())
    score1 = abs(k - e)
    score2 = abs(m - r)

    if k > e:
        score1 *= 508
    else:
        score1 *= 108

    if m > r:
        score2 *= 212
    else:
        score2 *= 305

    print((score1 + score2) * 4763)
    
elif T == 3:
    k, m, e = map(int, input().split())
    score1 = abs(k - e)
    score2 = m * 212

    if k > e:
        score1 *= 508
    else:
        score1 *= 108

    print((score1 + score2) * 4763)

elif T == 2:
    k, m = map(int, input().split())
    score1 = k * 508
    score2 = m * 212
    
    print((score1 + score2) * 4763)
    
elif T == 1:
    k = int(input())
    score1 = k * 508
    print(score1 * 4763)