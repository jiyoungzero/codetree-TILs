n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
    abs(x-center_x)+abs(y-center_y) < bomb_range

def bomb(center_x, center_y):
    global grid, next_grid
    bomb_range= grid[center_x][center_y]

    # step1. 폭탄이 터진 곳은 0으로 채우기
    for i in range(n):
        for j in range(n):
            if in_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0

    # step2. 터진 이후의 결과는 next_grid에 옮기기
    for j in range(n):
        next_row = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1 

    # step3. 원래의 grid로 다시 옮기기
    grid = [row[:] for row in next_grid]
    return 

r, c = tuple(map(int, input().split()))
bomb(r - 1, c - 1)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()