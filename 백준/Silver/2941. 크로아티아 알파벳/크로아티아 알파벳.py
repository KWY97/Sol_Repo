alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
N = len(word)

for alphabet in alphabets:
    word = word.replace(alphabet, '*')
print(len(word))