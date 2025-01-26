number_of_person = int(input())
people_list = []

for index in range(number_of_person):
    age, name = input().split()
    people_list.append((int(age), name, index))

people_list.sort(key=lambda x: (x[0], x[2]))

for age, name, index in people_list:
    print(age, name)