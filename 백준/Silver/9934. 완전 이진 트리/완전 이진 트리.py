def make_tree(node):
    global num
    if node <= (2 ** K) - 1:
        make_tree(node * 2)
        tree[node] = arr[num]
        num += 1
        make_tree(node * 2 + 1)

K = int(input())
arr = list(map(int, input().split()))
tree = [0] * ((2 ** K))
num = 0
make_tree(1)

for i in range(K):
    for j in range(2**i):
        print(tree[2**i + j], end = " ")
    print()