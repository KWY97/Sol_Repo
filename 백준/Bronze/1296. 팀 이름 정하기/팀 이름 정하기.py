yeondoo = input()
n = int(input())

maximum = -1
teams = [0] * n
max_team = ""

for i in range(n):
    teams[i] = (input())

teams.sort()

for team in teams:
    temp = yeondoo + team
    
    L = temp.count('L')
    O = temp.count('O')
    V = temp.count('V')
    E = temp.count('E')

    score = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    if maximum < score:
        maximum = score
        max_team = team
    elif maximum == score and team < max_team:
        max_team = team
    
print(max_team)