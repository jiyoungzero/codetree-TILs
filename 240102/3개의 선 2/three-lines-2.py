import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
line_cnt = 0 
visited = [False]*n

for i in range(n):
    x, y = points[i]
    flag = False
    for j in range(i+1, n):
        a, b = points[j]
        if not visited[j] and (x == a or b == y):
            flag = True
            visited[j] = True
    if flag:
        line_cnt += 1
if line_cnt == 3:
    print(1)
else:
    print(0)