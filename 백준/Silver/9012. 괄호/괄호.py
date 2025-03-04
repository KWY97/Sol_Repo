from collections import deque
queue = deque()

N = int(input())

for _ in range(N):
    queue = deque()
    arr = list(input())
    flag = 0
    
    for char in arr:
        if char == '(':
            queue.append(char)
        else:
            if len(queue) == 0:
                flag = 1
                print("NO")
                break
            else:
                queue.pop()
    if (len(queue) == 0) and (flag == 0):
        print('YES')
    elif (flag == 0):
        print('NO')