import heapq

n = int(input())
nums = list(map(int, input().split()))

heap = []
for i in range(n):
    for j in range(n):
        if len(heap) < n:
            heapq.heappush(heap, int(nums[i]/(j+1)))
        else:
            if heap[0] < int(nums[i]/(j+1)):
                heapq.heappop(heap)
                heapq.heappush(heap, int(nums[i]/(j+1)))


print(heap[0])