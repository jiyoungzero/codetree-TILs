import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**5)
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, cost = map(int, input().split())
    tree[a].append((b, cost))
    tree[b].append((a, cost))

def dfs(node, total_weight):
    for leaf, weight in tree[node]:
        if not visited[leaf]:
            visited[leaf] = True
            distance[leaf] = total_weight + weight
            dfs(leaf, distance[leaf])

distance = [-1]*(n+1)
visited = [False]*(n+1)
visited[1] = True
distance[1] = 0
dfs(1,0)

longest_node = distance.index(max(distance))

distance = [-1] * (n+1)
visited = [False]*(n+1)
visited[longest_node] = True
distance[longest_node] = 0
dfs(longest_node, 0)

print(max(distance))