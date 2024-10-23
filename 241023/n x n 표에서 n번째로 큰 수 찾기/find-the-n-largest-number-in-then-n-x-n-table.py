import heapq

n = int(input())
nums = list(map(int, input().split()))

heap = []
for i in range(n):
    for j in range(n):
        heapq.heappush(heap, -int(nums[i]/(j+1)))


for i in range(n-1):
    heapq.heappop(heap)
print(-heap[0])