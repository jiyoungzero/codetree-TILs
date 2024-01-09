import sys, heapq
input = sys.stdin.readline

n = int(input())
answer = 0
waiting = []
people = []
for i in range(n):
    a, t = tuple(map(int, input().split()))
    people.append((a, i+1, t))
people.sort()
exit_time = 0

for a, num, t in people:
    while exit_time <= a and waiting:
            (_, na, nt) = heapq.heappop(waiting)
            answer  = max(answer, exit_time-na)
            exit_time += nt

    if a > exit_time:
        exit_time += (a+t)
    else:
        heapq.heappush(waiting, (num, a, t))
print(answer)