import sys
input =sys.stdin.readline

n = int(input())
parent= list(map(int, input().split()))
graph = [[] for _ in range(n)]
del_node = int(input())
# 각 노드의 자식개수
leaf = [0]*n
root = 0

for i in range(n):
    if parent[i] == -1:
        root = i
        continue
    graph[parent[i]].append(i)



def dfs(x, parent):
    if len(graph[x]) == 0:
        leaf[x] += 1
    
    for y in graph[x]:
        dfs(y, x)
        leaf[x] += leaf[y]

for i in range(n):
    if del_node in graph[i]:
        graph[i].remove(del_node)


if del_node != root:
    dfs(root, -1) # root에서 타고 내려가면서 지워야 할 아이들 지우는 dfs

print(leaf[root])