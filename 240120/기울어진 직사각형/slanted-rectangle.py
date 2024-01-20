import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
up_down = [(-1, 1), (1, -1)]
left_right = [(-1, -1), (1, 1)]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_value(x, y, up_down_side, left_right_side):
    result = arr[x][y]
    for i in range(2):
        for _ in range(up_down_side):

            nx, ny = x + up_down[i][0], y+up_down[i][1]
            if not in_range(nx, ny):
                return False
            result += arr[nx][ny]
            x, y = nx, ny

        for _ in range(left_right_side):
            nx, ny = x + left_right[i][0], y+left_right[i][1]
            if not in_range(nx, ny):
                return 0
            result += arr[nx][ny]
            x, y = nx, ny
    return result-arr[x][y]


for i in range(2, n):
    for j in range(1, n-1):
        for up_down_side in range(1, n): 
            for left_right_side in range(1, n):
                answer = max(answer,get_value(i, j, up_down_side, left_right_side))

print(answer)