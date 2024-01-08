import sys
input = sys.stdin.readline

BLANK = 0
BLOCK = 1

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# (k-1)~(k+m-2)
def down_bar():
    for row in range(n):
        if 1 in arr[row][k-1:k+m-1]:
            return row - 1
    return n-1

def print_finish_arr():
    stop_row = down_bar()
    answer = [row[:] for row in arr]
    for col in range(k-1, k+m-1):
        answer[stop_row][col] = 1

    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=' ')
        print()

down_bar()
print_finish_arr()