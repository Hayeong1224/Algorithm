n = int(input())
tree = {} # 딕셔너리

for i in range(n):
  root, left, right = input().split()
  tree[root] = [left, right]

def preorder(node):
  if node == '.':
    return
    
  path.append(node)
  preorder(tree[node][0])
  preorder(tree[node][1])

def inorder(node):
  if node == '.':
    return

  inorder(tree[node][0])
  path.append(node)
  inorder(tree[node][1])

def postorder(node):
  if node == '.':
    return

  postorder(tree[node][0])
  postorder(tree[node][1])
  path.append(node)

path = []
preorder('A')
print(''.join(path))

path = []
inorder('A')
print(''.join(path))

path = []
postorder('A')
print(''.join(path))