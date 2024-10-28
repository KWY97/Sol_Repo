my_li = []

for _ in range(5):
    score = int(input())
    if score < 40:
        my_li.append(40)
    else:
        my_li.append(score)

print(sum(my_li) // len(my_li))