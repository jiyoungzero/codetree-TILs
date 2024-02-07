import sys
input = sys.stdin.readline 
MAX_VALUE = 10000
m = int(input())
nodes_info = [[0, 0] for _ in range(MAX_VALUE+1)] # in, out
edges = [[] for _ in range(MAX_VALUE+1)]
visited = [False]*(MAX_VALUE+1)
used = [False]*(MAX_VALUE+1)
is_tree = True
in_node = [0]*(MAX_VALUE+1)

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    used[a] = True
    used[b] = True

    in_node[b] +=1


def dfs(node):
    for leaf in edges[node]:
        if not visited[leaf]:
            visited[leaf] = True
            dfs(leaf)

root_cnt = 0
root = -1
for i in range(MAX_VALUE+1):
    if used[i] and in_node[i] == 0:
        root = i
        root_cnt +=1
    if root_cnt > 1:
        is_tree = False
        break
    
for i in range(MAX_VALUE+1):
    if root != i and used[i] and in_node[i] != 1:
        is_tree = False
        break

dfs(root)
for i in range(MAX_VALUE+1):
    if used[i] and not visited[i]:
        is_tree = False

if is_tree:
    print(1)
else:
    print(0)