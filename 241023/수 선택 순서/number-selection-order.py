import heapq 

n, x = map(int, input().split())
nums = list(map(int, input().split()))
heap = []
num2idx = []
for i, num in enumerate(nums):
    heapq.heappush(heap, -num)
    num2idx.append((num, i))

answer = 1
while num2idx:
    top = heap[0]
    num, idx = num2idx[0]
    # print(top, num, idx)

    # 현재 nums의 앞의 값이 heapq 앞 데이터와 같으며, num_idx와 x가 값이 같을 때 break 
    if num == -top and idx == x:
        break
    # 현재 nums의 앞의 값이 heapq 앞 데이터와 같을 때
    elif num == -top:
        # 1. nums.pop(0),
        num2idx.pop(0) 
        # 2. heapq.heappop(heap)
        heapq.heappop(heap)
        # 3. answer += 1
        answer += 1
    # 현재 nums의 앞이 값과 heapq 앞 데이터가 다를 때 
    elif num != -top:
        # 1. nums.pop(0) -> nums.append(ele)
        num, idx = num2idx.pop(0)
        num2idx.append((num, idx))
        # 2. answer += 1
        # answer += 1
    # print(answer)
print(answer)