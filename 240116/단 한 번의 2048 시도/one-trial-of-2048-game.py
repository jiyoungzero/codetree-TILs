import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(4)]
direction = {'L':3, 'R':1, "U":2, "D":4}
cur_dir = input().rstrip()


# 시계방향 90도 회전 
def rotate_90(array):
    tmp_array = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            tmp_array[i][j] = array[4-1-j][i]
    array = [row[:] for row in tmp_array]
    return array

# 아래로 압축
def down(array):
    tmp_array = [[0]*4 for _ in range(4)]
    for col in range(4):
        tmp_row = 3
        for row in range(3, -1, -1):
            if array[row][col]:
                tmp_array[tmp_row][col] = array[row][col]
                tmp_row -= 1
    array = [row[:] for row in tmp_array]
    return array


def compress(array):
    tmp_array = [[0]*4 for _ in range(4)]
    for col in range(4):
        tmp_row = 3
        for row in range(3, -1, -1):
            target = array[row][col] # 비교값
            if target == 0:continue
            elif target == array[row-1][col]:
                tmp_array[tmp_row][col] = target*2
                array[row][col] = 0
                array[row-1][col] = 0
                tmp_row -= 1
            else:
                tmp_array[tmp_row][col] = target
                array[row][col] = 0
                tmp_row -= 1

    array = [row[:] for row in tmp_array]
    return array

# 다시 4-direction[cur_dir]만큼 회전 후 출력
for _ in range(direction[cur_dir]):
    arr = rotate_90(arr)


arr = down(arr)
arr = compress(arr)


for _ in range(4-direction[cur_dir]):
    arr = rotate_90(arr)

for row in arr:
    print(*row)
print()