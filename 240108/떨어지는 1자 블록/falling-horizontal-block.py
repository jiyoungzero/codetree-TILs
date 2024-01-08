import sys
input = sys.stdin.readline

BLANK = 0
BLOCK = 1

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp_arr = [row[:] for row in arr]
stop_row = int(1e9)

# (k-1)~(k+m-2)
def down_bar():
    global stop_row
    for col in range(k-1, k+m-1):
        for row in range(n-1, -1, -1):
            if arr[row][col] == BLOCK:
                stop_row = min(stop_row, row-1)


def print_finish_arr(stop_row):
    answer = [row[:] for row in arr]
    for col in range(k-1, k+m-1):
        answer[stop_row][col] = 1

    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=' ')
        print()

down_bar()
print_finish_arr(stop_row)