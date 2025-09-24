def preorder(cur_node):
    if cur_node is None:
        return
    pre_out.append(cur_node)
    l, r = Tree[cur_node]
    preorder(l)
    preorder(r)

def inorder(cur_node):
    if cur_node is None:
        return
    l, r = Tree[cur_node]
    inorder(l)
    in_out.append(cur_node)
    inorder(r)

def postorder(cur_node):
    if cur_node is None:
        return
    l, r = Tree[cur_node]
    postorder(l)
    postorder(r)
    post_out.append(cur_node)

N = int(input())
Tree = {}

pre_out = []
in_out = []
post_out = []

for _ in range(N):
    root, left, right = input().split()
    Tree[root] = (None if left == '.' else left,
                  None if right == '.' else right)

preorder('A')
inorder('A')
postorder('A')

print(''.join(pre_out))
print(''.join(in_out))
print(''.join(post_out))