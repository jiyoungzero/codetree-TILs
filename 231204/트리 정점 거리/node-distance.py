import sys
input =sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = []

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # to, len
    graph[b].append((a, c))



for _ in range(m):
    visited = [False]*1001

    def getDistance(from_, to_, dist): 
        global answer
        if from_ == to_:
            answer.append(dist)
            return 
        for leaf in graph[from_]:
            if not visited[leaf[0]]:
                dist += leaf[1]
                visited[leaf[0]] = True

                getDistance(leaf[0], to_, dist)

                dist -= leaf[1]


    a, b = map(int, input().split())
    visited[a] = True
    getDistance(a,b,0)

for i in range(m):
    print(answer[i])