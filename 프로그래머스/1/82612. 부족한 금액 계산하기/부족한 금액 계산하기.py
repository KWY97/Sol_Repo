def solution(price, money, count):
    fee = 0
    
    for i in range(1, count+1):
        fee += price * i
    
    if money >= fee:
        return 0 
    return fee - money