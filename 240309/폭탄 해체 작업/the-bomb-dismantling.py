import sys
import heapq
input = sys.stdin.readline 

n = int(input())
bombs = [list(map(int, input().split())) for _ in range(n)]
bombs.sort(key = lambda x:(x[1]))
answer = 0
max_time = bombs[-1][1]

q = []
bomb_idx = n-1
for time in range(max_time, 0, -1):
    while bomb_idx >= 0 and bombs[bomb_idx][1] >= time:
        heapq.heappush(q, -bombs[bomb_idx][0])
        bomb_idx -= 1
    if q:
        answer += -heapq.heappop(q)
print(answer)