import sys
input = sys.stdin.readline
max_people = 0
people = 0

for _ in range(4):
    p_out, p_in = map(int, input().split())
    people += (p_in - p_out)

    if max_people < people:
        max_people = people
    
print(max_people)