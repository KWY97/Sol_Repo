def my_chicken(num_of_chicken, num_of_person):
    if num_of_chicken >= num_of_person:
        return num_of_person
    else:
        return num_of_chicken

N = int(input())
people = list(map(int, input().split()))
sum = 0

for person in people:
    sum += my_chicken(N, person)
print(sum)