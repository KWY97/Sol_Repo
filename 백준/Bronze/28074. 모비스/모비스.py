s = input()
saving = ['M', 'O', 'B', 'I', 'S']

for c in s:
    if saving:
        if c in saving:
            c_idx = saving.index(c)
            saving.pop(c_idx)

if saving:
    print("NO")
else:
    print("YES")