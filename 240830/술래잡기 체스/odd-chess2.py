import sys
input = sys.stdin.readline 
BLANK = (-1, -1)
MASTER = (-2, -2)

arr = []
for _ in range(4):
    row = []
    tmp = list(map(int, input().split()))
    for i in range(0, len(tmp)-1, 2):
        row.append((tmp[i], tmp[i+1]-1))
    arr.append(row)
dxs = [-1, -1,  0,  1, 1, 1, 0, -1]
dys = [ 0, -1, -1, -1, 0, 1, 1,  1]

answer = 0

def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def finish(x, y, d):
    for _ in range(4):
        x += dxs[d]
        y += dys[d]
        if in_range(x, y) and arr[x][y] != BLANK:
            return False
    return True

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def thief_can_go(x, y, d):
    return in_range(x, y) and arr[x][y] != MASTER


def move_thief():
    global arr
    nxt_arr = deep_copy(arr)

    def find_pos(idx):
        for i in range(4):
            for j in range(4):
                if (nxt_arr[i][j] != BLANK and nxt_arr[i][j] != MASTER) and nxt_arr[i][j][0] == idx:
                    return (i, j)
        return (-3, -3)

    for idx in range(1, 17):
        i, j = find_pos(idx)
        if (i, j) != (-3, -3):
            d = nxt_arr[i][j][1]
            original_d = d
            same = False
            while not thief_can_go(i+dxs[d], j+dys[d], d):
                d = (d+1)%8
                if d == original_d:
                    same = True
                    break
            if not same:
                ni, nj = i+dxs[d], j+dys[d]
                nxt_arr[ni][nj], nxt_arr[i][j] = (idx, d), nxt_arr[ni][nj]
    arr = deep_copy(nxt_arr)



def search_max_score(x, y, d, score):
    global answer, MASTER, arr

    # 더이상 움직일 곳이 없다면 return 
    if finish(x, y, d):
        answer = max(answer, score)
        return

    # 현재 턴에 움직일 수 있는 곳은 전부 탐색 
    for dist in range(1, 4):
        nx, ny = x + dxs[d] * dist, y + dys[d]*dist
        # 술래가 이동할 수 없다면, 패스
        if not in_range(nx, ny) or arr[nx][ny] == BLANK:continue

        # 더 탐색을 진행할 경우, tmp_arr로 이전 배열 상태 저장
        prev_arr = deep_copy(arr)

        # 해당 위치의 도둑말을 잡고
        n_score, n_d = arr[nx][ny]
        arr[x][y] = BLANK
        arr[nx][ny] = MASTER
        # print((x, y), "->", (nx, ny), n_d)

        # 모든 도둑말을 움직임 
        move_thief()

        # 그 다음 탐색 시작
        search_max_score(nx, ny, n_d, score + n_score)

        # 이전 배열 상태 되돌리기, 위치
        arr = deep_copy(prev_arr)

init_score, init_dir = arr[0][0]

arr[0][0] = MASTER
move_thief()
search_max_score(0, 0, init_dir, init_score)

print(answer)