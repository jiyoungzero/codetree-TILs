import sys, heapq
input = sys.stdin.readline 
MAX_VALUE = sys.maxsize

n, m = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [MAX_VALUE] * (n+1)

def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue

        for i in graph[cur]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijk(1)
for i in range(2, n+1):
    print(distance[i] if distance[i] < MAX_VALUE else -1)