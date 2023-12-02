import sys
input =sys.stdin.readline


m = int(input())
graph = [[] for _ in range(10001)]
flag1, flag2, flag3 = False, False, True
root = 0
nodes = set()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    nodes.add(a)
    nodes.add(b)

# 진입차수 세기
in_node =[0] *(m+2)

for g in graph:
    for node in g:
        in_node[node] += 1

in_node[0] = -1 # 루트노드로 잡히지 않게.
# 진입차수가 0인 것이 하나만 있는지 체크
if in_node.count(0) == 1:
    flag1 = True
    root = in_node.index(0)


# 조건2
if in_node.count(1) == m:
    flag2 = True

# 조건3
visited = [False]*int(100001)
def dfs(x):
    for y in graph[x]:
        if visited[y] : continue
        visited[y] = True
        dfs(y)
    return

dfs(root)
for node in nodes:
    if not root and not visited[node]:
        flag3 = False


if flag1 and flag2 and flag3:
    print(1)
else:
    print(0)