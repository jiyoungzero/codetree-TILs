import sys
input = sys.stdin.readline 
import heapq

n, tmax = map(int, input().split())
answer = sys.maxsize
arr = [int(input()) for _ in range(n)]


def is_possible(k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])

    idx = k
    while idx < n:
        nxt = heapq.heappop(heap)
        heapq.heappush(heap, nxt + arr[idx])
        idx += 1

    return max(heap) <= tmax


    
l, r = 0, n
while l <= r:
    mid = (l+r)//2
    if is_possible(mid): # k = mid 일 때 걸리는 시간이 tmax를 넘지 않을 때
        r = mid - 1
        answer = min(answer, mid)
    else:
        l = mid + 1
print(answer)