li = []

for _ in range(5):
    num = int(input())
    li.append(num)

li.sort()

print(int(sum(li)/5))
print(li[2])