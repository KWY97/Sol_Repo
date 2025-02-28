# 첫 줄에는 
# $1$부터 
# $N$까지 수의 합 
# $1+2+\cdots+N$을 출력하세요.

# 둘째 줄에는 
# $1$부터 
# $N$까지 수의 합을 제곱한 수 
# $(1+2+\cdots+N)^2$을 출력하세요.

# 셋째 줄에는 
# $1$부터 
# $N$까지 수의 세제곱의 합 
# $1^3+2^3+\cdots+N^3$을 출력하세요.

def first(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

def second(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i**3
    return sum

N = int(input())
a = first(N)
print(a)
print(a*a)
print(second(N))