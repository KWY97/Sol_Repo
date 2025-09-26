def count_leaf():
    if del_node == root:
        return 0

    leaf_cnt = 0
    stack = [root]

    while stack:
        u = stack.pop()

        pushed = False
        for v in children[u]:
            if v == del_node:
                continue
            stack.append(v)
            pushed = True

        if not pushed:
            leaf_cnt += 1

    return leaf_cnt

N = int(input())
parent = list(map(int, input().split()))
del_node = int(input())

children = [[] for _ in range(N)]
for i, p in enumerate(parent):
    if p == -1:
        root = i
    else:
        children[p].append(i)

print(count_leaf())

