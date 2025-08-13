def solution(bandage, health, attacks):
    n = (max(attacks))[0]
    cur_healths = [[health]] + [[] for _ in range(n+1)]
    cur_second = 0
    duration = 0
    flag = 1

    while cur_second != n:
        if flag == 0:
            break
            
        cur_second += 1
        duration += 1
        
        for attack in attacks:
            if cur_second > attack[0]:
                continue

            if attack[0] == cur_second:
                cur_health = cur_healths[cur_second - 1][0] - attack[1]
                if cur_health <= 0:
                    ans = -1
                    flag = 0
                else:
                    cur_healths[cur_second].append(cur_health)
                    duration = 0
            else:
                cur_health = cur_healths[cur_second - 1][0] + bandage[1]
                
                if duration == bandage[0]:
                    cur_health += bandage[2]
                    duration = 0
                
                if cur_health >= health:
                    cur_health = health
                
                cur_healths[cur_second].append(cur_health)
    if flag == 1:
        ans = cur_healths[n][0]
    print(cur_healths)
                    
    return ans