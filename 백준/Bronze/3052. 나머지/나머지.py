my_set = set()

for _ in range(10):
    n = int(input())
    a = n % 42
    my_set.add(a)

print(len(my_set))