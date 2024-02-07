import sys
input = sys.stdin.readline 


n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    for leaf in tree[node]:
        if parent[leaf] == 0:
            parent[leaf] = node
            dfs(leaf)
dfs(1)
for ele in parent[2:]:
    print(ele)