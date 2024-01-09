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
people.append((int(1e9), int(1e9), 0))

for a, num, t in people:
    # 웨이팅도 있고, 이제 내가 들어갈 수 있을 때,
    while exit_time <= a and waiting:
            (_, na, nt) = heapq.heappop(waiting)
            answer  = max(answer, exit_time-na)
            exit_time += nt

    # 웨이팅도 없고 내가 들어갈 수 있을때
    if a > exit_time:
        exit_time += (a+t)
    # 웨이팅은 없으나 내가 들어갈 수 없을 때
    else:
        heapq.heappush(waiting, (num, a, t))
print(answer)