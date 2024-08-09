import sys
input = sys.stdin.readline 
import heapq

n = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(n)] # 점수, 시간제한

# 1. 가장 늦은 시간 순으로 정렬
# 2. 정렬된 배열을 우선순위 큐에 저장하여 가장 큰 점수를 바로 꺼내기
bombs.sort(key = lambda x:(-x[1]))
max_time = bombs[0][1] 

heap = []
idx = 0
answer = 0
for time in range(max_time, 0, -1):
    
    while True:
        if n <= idx or time != bombs[idx][1]:break
        s, l = bombs[idx]
        heapq.heappush(heap, (-s, l))
        # print(time, idx)
        idx += 1
    
    if heap:
        s, l = heapq.heappop(heap)
        answer += (-s)
print(answer)