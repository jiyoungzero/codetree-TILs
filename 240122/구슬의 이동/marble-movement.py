# 변수 선언 및 입력:

dir_mapper = {
    "U": 0,
    "R": 1,
    "L": 2,
    "D": 3
}

n, m, t, k = tuple(map(int, input().split()))
grid = [[[] for _ in range(n)] for _ in range(n)]
next_grid = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):

    r, c, d, v = tuple(input().split())
    r, c, v = tuple(map(int, [r, c, v]))

    # 살아남는 구슬의 우선순위가 더 빠른 속도, 더 큰 번호 이므로
    # (속도, 방향, 번호) 순서를 유지합니다.
    grid[r - 1][c - 1].append((v, i + 1, dir_mapper[d]))


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def next_pos(x, y, v, move_dir):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    for _ in range(v):
        nx, ny = x+ dxs[move_dir], y + dys[move_dir]
        if not in_range(nx, ny):
            move_dir = (3-move_dir)
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
        x, y = nx, ny
    return (x, y, move_dir)



def move():
    for x in range(n):
        for y in range(n):
            for v, num, move_dir in grid[x][y]:
                nx, ny, ndir = next_pos(x, y, v, move_dir)
                next_grid[nx][ny].append((v, num, ndir))

def bomb():
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) >= k:
                next_grid[i][j].sort(lambda x: (-x[0], -x[1]))
                while len(next_grid[i][j]) > k:
                    next_grid[i][j].pop()

def simulate():
    # next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []
    # 1) 구슬 전부 움직이기
    move()

    # 2) k개 이상인 곳 bomb
    bomb()

    # 3) next_grid값은 grid로 옮기기
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

# t초에 걸쳐 시뮬레이션을 반복합니다.
for _ in range(t):
    simulate()

ans = sum([
    len(grid[i][j])
    for i in range(n)
    for j in range(n)
])
print(ans)