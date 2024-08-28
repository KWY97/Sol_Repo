s = input()
dic = {2: ['A','B','C'], 3: ['D','E','F'], 4: ['G','H','I'], 5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7:['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}
sum = 0

for v in s:
    for i in range(2, 10):
        if v in dic[i]:
            sum += i
print(sum+len(s))