import sys
input = sys.stdin.readline 
import heapq

n = int(input())
heap = []
answer = 0

for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(heap, (e, s))

last_time = 0
while heap:
    e, s = heapq.heappop(heap)
    if last_time <= s:
        answer += 1
        last_time = e

print(n - answer)