import sys
input = sys.stdin.readline

def myFunc():
    start = max(0, N - (len(str(N)) * 9))

    for number in range(start, N):
        my_sum = 0 
        for num in str(number):
            my_sum += int(num)
        if (number + my_sum == N):
            return number
    return 0
    
N = int(input())
print(myFunc())