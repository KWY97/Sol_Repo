def dfs(ans, cnt, n, nums, t):
    global ans_cnt
    
    if cnt == n:
        if ans == t:
            ans_cnt += 1
        return
    
    dfs(ans + nums[cnt], cnt + 1, n, nums, t)
    dfs(ans - nums[cnt], cnt + 1, n, nums, t)
            

def solution(numbers, target):
    N = len(numbers)
    dfs(0, 0, N, numbers, target)
    answer = ans_cnt
    
    return answer

ans_cnt = 0