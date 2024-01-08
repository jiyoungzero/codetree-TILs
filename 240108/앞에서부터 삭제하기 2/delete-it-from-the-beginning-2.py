import sys, heapq
input =sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0

for k in range(1, n-1):
    heap = arr[k:]
    heapq.heapify(heap)
    
    heapq.heappop(heap)
    answer = max(answer, sum(heap)/len(heap))


print(f"{answer:.2f}")