import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, r_dir = map(int, input().split())
# r_dir == 0 : 반시계 방향 
# r_dir == 1 : 시계 방향
m_dir = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
m_lst = [m1, m2, m3, m4-1]
r -= 1
c -= 1

def get_que():
    copy_r, copy_c = r, c
    que = deque()
    que.append(arr[r][c])

    for k in range(4):
        for _ in range(m_lst[k]):
            nr, nc = copy_r + m_dir[k][0], copy_c+m_dir[k][1]
            que.append(arr[nr][nc])
            copy_r, copy_c = nr, nc
    return que

def rotate(r_dir):
    q = get_que()
    if r_dir == 0: 
        tmp = q.pop()
        q.appendleft(tmp)
    else:
        tmp = q.popleft()
        q.append(tmp)
    return q 

def rewrite():
    global arr, r, c
    copy_r, copy_c = r, c
    new_q = rotate(r_dir)
    arr[r][c] =  new_q.popleft()  
    for k in range(4):
        for _ in range(m_lst[k]):
            nr, nc = copy_r + m_dir[k][0], copy_c+m_dir[k][1]
            arr[nr][nc] = new_q.popleft()
            copy_r, copy_c = nr, nc
    return 

rewrite()

# 정답 출력
for row in arr:
    print(*row)