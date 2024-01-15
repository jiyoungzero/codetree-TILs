import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(4)]
direction = {'L':3, 'R':1, "U":4, "D":2}
cur_dir = input()


# 시계방향 90도 회전 
def rotate_90(array):
    tmp_array = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            tmp_array[i][j] = array[4-1-j][i]
    array = [row[:] for row in tmp_array]
    return array

# 아래로 압축

# 다시 4-direction[cur_dir]만큼 회전 후 출력