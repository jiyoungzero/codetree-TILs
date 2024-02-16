import sys
input = sys.stdin.readline 
import heapq 

n = int(input())
computers = []
assigned = [0]*n
segments = []
for i in range(n):
    p, q = map(int, input().split())
    heapq.heappush(computers, i+1)
    segments.append((p, q))


points = []
for idx, segment in enumerate(segments):
    start, end = segment
    points.append((start, 1, idx))
    points.append((end, -1, idx))

points.sort()
for point in points:
    x, flag, idx = point
    if flag == 1:
        nxt_computer = heapq.heappop(computers)
        assigned[idx] = nxt_computer
    else:
        return_computer = assigned[idx]
        heapq.heappush(computers, return_computer)

print(*assigned)