import sys
input = sys.stdin.readline 


n , m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0,0,1,-1], [1,-1,0,0]
visited = [[False]*m for _ in range(n)]

# k 초과인 뭉탱이의 개수 뭉탱이의 수는 많으며, 뭉탱이의 수가 같으면 k가 작은 것을 선택 
# if safe_zone_tmp == safe_zone and k < k_tmp : break
answer_k = int(1e9)
answer_safe_zone = -1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y, k):
    global safe_zone, visited
    for d in range(4):
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny):
            continue 
        if not visited[nx][ny] and arr[nx][ny] > k:
            visited[nx][ny] = True
            dfs(nx, ny, k)

for k in range(100, 0, -1):
    safe_zone = 0 
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] > k:
                visited[i][j] = True
                dfs(i, j, k)
                safe_zone += 1
    if answer_safe_zone <= safe_zone:
        answer_safe_zone = safe_zone
        answer_k = k
print(answer_k, answer_safe_zone)