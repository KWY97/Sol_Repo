N = input()
F = int(input())

temp = N[0:-2] # 끝 두자리 제외
start = "00"

num = int(temp+start)

while True:
    if num % F == 0:
        print((str(num))[-2:])
        break
    else:
        num += 1