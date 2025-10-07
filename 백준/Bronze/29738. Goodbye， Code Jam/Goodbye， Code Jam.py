t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    if n <= 25:
        y = "World Finals"
    elif n <= 1000:
        y = "Round 3"
    elif n <= 4500:
        y = "Round 2"
    else:
        y = "Round 1"
    print(f"Case #{tc}: {y}")
