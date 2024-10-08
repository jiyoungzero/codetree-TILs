import sys
input = sys.stdin.readline 
import heapq

q = int(input())
cities = []
distance = []
n, m = 0, 0
s_heap = [] # 관리목록
start = 0 # 처음 출발지는 0
is_made = []
is_canceled = []

class Stock:
    def __init__(self, id, revenue, to_, profit):
        self.id = id 
        self.revenue = revenue
        self.to_ = to_
        self.profit = profit
    
    def __lt__(self, other):
        if self.profit == other.profit:
            return self.id < other.id 
        return self.profit > other.profit

def dijkstra(start):
    global distance
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue 
        for leaf in cities[now]:
            cost = leaf[1] + dist
            if cost < distance[leaf[0]]:
                distance[leaf[0]] = cost
                heapq.heappush(que, (distance[leaf[0]], leaf[0]))

def find_best_stock():
    global is_canceled
    while s_heap:
        top = s_heap[0]
        if distance[top.to_] == int(1e9) or top.profit < 0:
            break
        top = heapq.heappop(s_heap)
        if not is_canceled[top.id]:
            is_canceled[top.id] = True
            return top.id
    return -1



for _ in range(q):
    cmd = tuple(map(int, input().split()))
    if cmd[0] == 100:
        n, m = cmd[1], cmd[2]
        is_made = [False]*(n+1)
        is_canceled = [False]*(n+1)
        distance = [int(1e9)]*(n+1)
        cities = [[] for _ in range(n+1)]
        for i in range(3, len(cmd), 3):
            v1, v2, w = cmd[i], cmd[i+1], cmd[i+2]
            if v1 == v2: cities[v1].append((v2, w))
            cities[v1].append((v2, w))
            cities[v2].append((v1, w))
    elif cmd[0] == 200:
        idx, revenue, to_ = cmd[1], cmd[2], cmd[3]
        is_made[idx] = True
        dijkstra(start)
        heapq.heappush(s_heap, Stock(idx, revenue, to_, revenue-distance[to_]))
    elif cmd[0] == 400:
        print(find_best_stock())
    elif cmd[0] == 300:
        del_id = cmd[1]
        if is_made[del_id]:
            is_canceled[del_id] = True 
    else:
        start = cmd[1]
        distance = [int(1e9)]*(n+1)
        dijkstra(start)
        nxt_s_heap = []
        for ele in s_heap:
            ele.profit = revenue - distance[ele.to_]
            nxt_s_heap.append(Stock(ele.id, ele.revenue, ele.to_, ele.profit))
        s_heap = nxt_s_heap[:]
        heapq.heapify(s_heap)
        # for ele in s_heap:
        #     print(ele.id, ele.revenue, ele.to_, distance[ele.to_], ele.profit)