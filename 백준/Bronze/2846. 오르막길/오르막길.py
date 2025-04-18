N = int(input())
arr = list(map(int, input().split()))
answer = 0
answers = []

for i in range(N-1):
    if arr[i] < arr[i+1]:
        answer += arr[i+1] - arr[i]
    else:
        answers.append(answer)
        answer = 0
    
    if arr[N-2] < arr[N-1]:
        answers.append(answer) 

print(max(answers))