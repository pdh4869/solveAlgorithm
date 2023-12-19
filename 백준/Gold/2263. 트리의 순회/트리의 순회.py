import sys

sys.setrecursionlimit(10**6)

n = int(input())

inorder = list(map(int, sys.stdin.readline().split()))
postorder  = list(map(int, sys.stdin.readline().split()))

node = [0] * (n+1)

for i in range(n):
    node[inorder[i]] = i
    
def pre(in_start, in_end, post_start, post_end):
    if (in_start > in_end) and (post_start > post_end):
        return
    
    root = postorder[post_end]
    left = node[root] - in_start
    right = in_end - node[root]
    
    print(root, end=' ')
    pre(in_start, in_start+left - 1, post_start, post_start + left - 1)
    pre(in_end - right + 1, in_end, post_end - right, post_end - 1)
    
pre(0, n-1, 0, n-1)