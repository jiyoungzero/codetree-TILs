import sys, heapq
input =sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
heap = []
heapq.heappush(heap, arr[-1])
answer = 0
prefix_sum = heap[0]
prefix_cnt = 0

for i in range(n- 2, 0, -1):
    heapq.heappush(heap, arr[i])
    prefix_sum += arr[i]
    prefix_cnt += 1

    min_val = heap[0]
    answer = max(answer, (prefix_sum-min_val)/(prefix_cnt))


print(f"{answer:.2f}")