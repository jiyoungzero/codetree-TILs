import sys
input = sys.stdin.readline 
import heapq
from bisect import bisect_left, bisect_right

c, n = map(int, input().split())
reds = [int(input()) for _ in range(c)]
reds_heap = []
for i, t in enumerate(reds):
    heapq.heappush(reds_heap, (t, i))

blacks = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

reds.sort()
blacks.sort(key = lambda x : (x[1])) # b가 작은 값부터 보면서 a <= 를 만족하는 가장 작은 t값을 매칭

# print(reds)
# print(blacks)

for a, b in blacks:
    idx = bisect_left(reds, a)
    
    if idx < len(reds):
        if reds[idx] <= b:
            del reds[idx]
            answer += 1

print(answer)