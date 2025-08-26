ans = 0

for i in range(3, 0, -1):
    n = input()
    if ans != 0:
        continue

    if n.isdigit():
        ans += int(n) + i

if ans % 3 == 0 and ans % 5 == 0:
    print('FizzBuzz')
elif ans % 3 == 0:
    print('Fizz')
elif ans % 5 == 0:
    print('Buzz')
else:
    print(ans)