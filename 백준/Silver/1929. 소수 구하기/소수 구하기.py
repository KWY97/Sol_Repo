def find_prime_number(start, end):
    prime_number = []

    for i in range(start, end + 1):
        if i < 2:
            continue

        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_number.append(i)

    return prime_number


M, N = map(int, input().split())
answer = find_prime_number(M, N)
for k in answer:
    print(k)