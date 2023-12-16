import sys

n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]
    
def pre(root):
    if root != '.':
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])

def in_(root):
    if root != '.':
        in_(tree[root][0])
        print(root, end='')
        in_(tree[root][1])
        
def post(root):
    if root != '.':
        post(tree[root][0])
        post(tree[root][1])
        print(root, end='')
        
pre('A')
print()
in_('A')
print()
post('A')