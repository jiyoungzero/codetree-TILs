import sys, heapq
input = sys.stdin.readline


n = int(input())
people = []
answer = 0
for i in range(n):
    a, t = map(int, input().split())
    people.append((i, a, a+t))
people.sort(key=lambda x : x[1])
waiting = []
visited = [False]*n

enter = people[0]
idx, in_, out_ = enter
visited[idx] = True
key = False

for i in range(n):
    if visited[people[i][0]]:continue
    if (not visited[people[i][0]] and key):
        nnidx, nnin_, nnout_ = people[i]
        answer = max(answer, out_-nnin_)
        idx, in_, out_ = nnidx, nnin_, nnout_ 
        visited[idx] = True
        print("dddd")

    if not key:
        # waiting걸기
        for j in range(n):
            if not visited[people[j][0]]:
                if people[j] in waiting:continue
                if people[j][1] < out_:
                    heapq.heappush(waiting, people[j])
            
    if waiting:
        print(waiting)
        nxt = heapq.heappop(waiting)

        nidx, nin_, nout_ = nxt
        answer = max(answer, out_-nin_)
        idx, in_, out_ = nidx, nin_, nout_
        visited[idx] = True
        print(visited, idx, nidx)

    if not waiting:
        key = True
    print(visited)

print(answer)