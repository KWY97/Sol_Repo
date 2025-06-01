tc = int(input())

for _ in range(tc):
    A, B = map(int, input().split())

    # 최소 공배수를 구하기 위한 두 자연수의 곱
    temp = A * B
    
    if A < B:
        A, B = B, A

    # 최대 공약수를 구한다.
    while True:
        r = A % B
        if r == 0:
            break
        else:
            A = B
            B = r
    
    # 최소 공배수
    print(temp // B)