import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
answer = 0
for _ in range(n-1):
    a, b, cost = map(int, input().split())
    tree[a].append((b, cost))
    tree[b].append((a, cost))

def dfs(node, target, dist):
    global answer
    if node == target:
        answer = dist
        return 
    for leaf, cost in tree[node]:
        if not visited[leaf]:
            visited[leaf] = True
            dfs(leaf, target, dist+cost)

for _ in range(m):
    answer = 0
    visited = [False]*(n+1)
    a, b = map(int, input().split())
    
    visited[a] = True
    dfs(a, b, 0)
    print(answer)