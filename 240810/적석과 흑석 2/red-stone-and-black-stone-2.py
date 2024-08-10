import sys
input = sys.stdin.readline 
import heapq

c, n = map(int, input().split())
reds = [int(input()) for _ in range(c)]
blacks = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

reds.sort()
blacks.sort(key = lambda x : (x[1])) # b가 작은 값부터 보면서 a <= 를 만족하는 가장 작은 t값을 매칭

heap = []
idx = 0
for a, b in blacks:
    while idx < c and a <= reds[idx] <= b:
        heapq.heappush(heap, reds[idx])
        idx += 1

    if heap:
        answer += 1
        heapq.heappop(heap)
print(answer)