import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
arr = list(map(int, input().split()))
for ele in arr:
    heapq.heappush(heap, -ele)

while len(heap) > 1:
    max1 = -heapq.heappop(heap)
    max2 = -heapq.heappop(heap)
    target = abs(max1-max2)
    if target != 0:
        heapq.heappush(heap, -target)

print(-heap[0] if len(heap) > 0 else -1)