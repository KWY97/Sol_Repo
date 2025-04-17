N = int(input())

students = []

for _ in range(N):
    country, student, score = map(int, input().split())
    students.append([score, country, student])

students.sort(reverse=True)

result = []
country_count = {}

for score, country, student in students:
    if country_count.get(country, 0) < 2:
        result.append([country, student])
        country_count[country] = country_count.get(country, 0) + 1
    if len(result) == 3:
        break

for country, student in result:
    print(country, student)