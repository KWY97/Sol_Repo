T = int(input())

for _ in range(T):
    year = input()

    if (int(year) + 1) % int(year[-2:]) == 0:
        print("Good")
    else:
        print("Bye")