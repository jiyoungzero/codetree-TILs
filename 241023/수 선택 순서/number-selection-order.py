import heapq

n, x = map(int, input().split())
heap = []
nums = list(map(int, input().split()))
answer = 1
for num in nums:
    heapq.heappush(heap, -num)

while nums:
    ele = nums.pop(0)
    if ele == x:
        break 
    elif ele == -heap[0]:
        heapq.heappop(heap)
    else:
        nums.append(ele)
    answer += 1


print(answer)