import sys
input = sys.stdin.readline

number_of_people = int(input())
people_list = []
rank_list = []

for _ in range(number_of_people):
    weight, height = map(int, input().split())
    people_list.append([weight, height])

for i in people_list:
    rank = 1
    for j in people_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    rank_list.append(rank)

print(*rank_list)