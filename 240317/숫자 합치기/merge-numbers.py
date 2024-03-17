import heapq
n = int(input())
arr = list(map(int, input().split()))
answer = 0


q = []
for ele in arr:
    heapq.heappush(q,ele)

while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, (a+b))
    answer += (a+b)
print(answer)