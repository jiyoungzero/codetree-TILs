import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
point_x = defaultdict(int)
point_y = defaultdict(int)

line_cnt = 0
visited = [False]*(n)
set_point = set()

for i in range(n):
    visited[i] = True
    for j in range(i+1, n):
        if points[i][0] == points[j][0]: # x좌표
            if not visited[j]:
                visited[j] = True
                set_point.add(points[j][0])
        elif points[i][1] == points[j][1]: # y좌표
            if not visited[j]:
                visited[j] = True
                flag = True
                set_point.add(points[j][0])
print(set_point)
print(1 if len(set_point) == 3 else 0)