hambergers = []
drinks = []

for _ in range(3):
    hamberger = int(input())
    hambergers.append(hamberger)

for _ in range(2):
    drink = int(input())
    drinks.append(drink)

print(min(hambergers) + min(drinks) - 50)