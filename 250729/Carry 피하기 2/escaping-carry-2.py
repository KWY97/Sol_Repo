def check_carry(n1, n2, n3):
    a, b, c = n1, n2, n3

    while a > 0 or b > 0 or c >0:
        d1 = a % 10
        d2 = b % 10
        d3 = c % 10

        if d1 + d2 + d3 >= 10:
            return True

        a //= 10
        b //= 10
        c //= 10

    return False

N = int(input())
numbers = [int(input()) for _ in range(N)]
ans = None

# 3개의 수 뽑기
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            # carry 발생 여부 확인
            carry = check_carry(numbers[i], numbers[j], numbers[k])
            # 만약 carry가 발생하지 않는다면
            if not carry:
                # 그 중 최대값 구하기
                if ans is None or ans < numbers[i] + numbers[j] + numbers[k]:
                    ans = numbers[i] + numbers[j] + numbers[k]

# 모든 수 쌍에서 carry가 발생한 경우
if ans is None:
    ans = -1

print(ans)