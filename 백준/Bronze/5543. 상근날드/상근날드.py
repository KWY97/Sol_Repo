hambergers = []
drinks = []

for i in range(5):
    if i == 0 or i == 1 or i == 2:
        hambergers.append(int(input()))
    else:
        drinks.append(int(input()))

print(min(hambergers) + min(drinks) - 50)