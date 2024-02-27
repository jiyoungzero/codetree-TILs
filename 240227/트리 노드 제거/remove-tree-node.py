import sys
input = sys.stdin.readline 

n = int(input())
parents = list(map(int, input().split()))
tree = [[] for _ in range(n)]
remove_node = int(input())
root_node = -1
is_deleted = [False]*n
answer = 0

for child, parent in enumerate(parents):
    if parent == -1:
        root_node = child
    else:
        tree[parent].append(child)


# 지울 노드 이후에 나오는 노드의 수
def dfs(node):
    global answer
    if is_deleted[node]:return
    
    is_leaf = True
    for leaf in tree[node]:
        if not is_deleted[leaf]:
            dfs(leaf)
            is_leaf = False

    if is_leaf:
        answer += 1

is_deleted[remove_node] = True
dfs(root_node)
print(answer)