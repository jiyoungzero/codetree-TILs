import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
que = deque()
que.append((n, 0))
visited = [n]
answer = 0

def bfs():
    global answer
    while que:
        now_num, time= que.popleft()
        if now_num == 1:
            answer = time
            return 

        if now_num//3 not in visited and now_num % 3 == 0:
            visited.append(now_num//3)
            que.append((now_num//3, time+1))
        if now_num//2 not in visited and now_num % 2 == 0:
            visited.append(now_num//2)
            que.append((now_num//2, time+1))
        if now_num-1 not in visited:
            visited.append(now_num-1)
            que.append((now_num-1, time+1))
        if now_num+1 not in visited:
            visited.append(now_num+1)
            que.append((now_num+1, time+1))

bfs()
print(answer)