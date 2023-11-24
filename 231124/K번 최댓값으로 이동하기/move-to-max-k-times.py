import sys
input =sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
sr -= 1
sc -= 1

# 자신보다 작은지 -> 최대값을 candidates 리스트에 넣기
# 행기준으로, 열기준으로 오름차순 정렬 
dxs, dys = [0,0,1,-1],[1,-1,0,0]

def bfs(r, c, target):
    global visited, candidates
    que = deque([(r,c)])
    visited[r][c] = True

    while que:
        nr, nc = que.popleft()
        for k in range(4):
            if not visited[nr][nc]:continue
            elif nr < 0 or nc < 0 or n <= nr or n <= nc:continue
            else:
                if arr[nr][nc] < target:
                    if len(candidates) == 0:
                        candidates.append((nr, nc))
                    elif (arr[candidates[0][0]][candidates[0][1]]) < arr[nr][nc]:
                        candidates = [(nr, nc)]
                        visited[nr][nc] = True
                        que.append((nr, nc))
                    elif (arr[candidates[0][0]][candidates[0][1]]) == arr[nr][nc]:
                        candidates.append((nr,nc))
                        visited[nr][nc] = True
                        que.append((nr, nc))


        candidates.sort(key = lambda x: (x[0], x[1]))     

        return candidates[0] if len(candidates) > 0 else -1

target = arr[sr][sc]
r, c = 0, 0
for _ in range(k):
    visited = [[False]*n for _ in range(n)]
    candidates = []
    result = bfs(sr, sc, target)
    if result == -1:
        print(sr, sc)
        break
    else:
        sr, sc = result[0], result[1]
if result != -1:
    print(sr, sc)