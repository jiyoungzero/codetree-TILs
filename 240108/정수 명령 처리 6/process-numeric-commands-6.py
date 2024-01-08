import heapq, sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    tmp = (input().split())
    if len(tmp) > 1:
        heapq.heappush(heap, -int(tmp[1]))
    else:
        if tmp[0] == 'size':
            print(len(heap))
        elif tmp[0] == 'pop':
            print(-heapq.heappop(heap))
        elif tmp[0] == 'top':
            print(-heap[0])
        else:
            if len(tmp) == 0:
                print(1)
            else:
                print(0)