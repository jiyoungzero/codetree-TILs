import sys
input = sys.stdin.readline


n = int(input())
parent = list(map(int, input().split()))
del_node = int(input())
leaf = [0]*n 
root = 0
graph = [[] for _ in range(n)]

for i in range(n):
    graph[parent[i]].append(i)

def dfs(x, parent):
    global leaf
    if not graph[x]:
        leaf[x] += 1
    for y in graph[x]:
        dfs(y, x)
        leaf[x] += leaf[y]


def solution():
    for i in range(n):
        if del_node in graph[i]:
            graph[i].remove(del_node)
    
    if root != del_node:
        dfs(root, -1)
solution()
print(leaf[root])