import sys
input = sys.stdin.readline 

n = int(input())
parents = list(map(int, input().split()))
tree = [[] for _ in range(n)]
remove_node = int(input())

visited = [False]*n
for child, parent in enumerate(parents):
    if parent == -1:continue

    tree[parent].append(child)


# 지울 노드 이후에 나오는 노드의 수
def dfs(node):
    for leaf in tree[node]:
        if not visited[leaf]:
            visited[leaf] = True
            dfs(leaf)

visited[remove_node] = True
dfs(remove_node)
print(max(n-visited.count(True)-1,0))