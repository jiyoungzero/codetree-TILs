import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
sr -= 1
sc -= 1

dxs, dxy = [0,0,1,-1], [1,-1,0,0]
def possible(x, y):
    # 갈 수 있는 애들의 위치를 넣고 정렬
    target = arr[x][y]
    que = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] < target:
                que.append((i,j))
    return que.sort(key = lambda x:(x[0], x[1]))

for _ in range(k):
    result = possible(sr,sc)
    if len(result) > 0:
        sr, sc = result[0]
        print(sr, sc)
    else:
        break
print(sr, sc)