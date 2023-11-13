import sys
input = sys.stdin.readline


arr = [list(map(int, input().split())) for _ in range(19)]
answer = 0

def in_range(a, b):
    return 0<= a <19 and 0<= b< 19

# 검 승 : 1
# 흰 승 : 2
# 무승부 : 0
# 무승부가 아닌 승자의 가운데 위치 바둑알 (i, j)

horiz = [(0, -2), (0,-1), (0, 1), (0, 2)]
verti = [(-2,0), (-1,0),(1,0),(2,0)]
left_diag = [(-2,-2), (-1,-1),(1,1),(2,2)]
right_diag = [(-2,2),(-1,1),(1,-1),(2,-2)]

def check_horiz(i, j):
    start = arr[i][j]
    for h in horiz:
        x, y = h
        if not in_range(i+x, j+y):
            return False
        elif start != arr[i+x][j+y]:
            return False
    return True

def check_verti(i, j):
    start = arr[i][j]
    for v in verti:
        x, y = v
        if not in_range(i+x, j+y):
            return False
        elif start != arr[i+x][j+y]:
            return False
    return True

def check_left_diag (i, j):
    start = arr[i][j]
    for ld in left_diag :
        x, y = ld
        if not in_range(i+x, j+y):
            return False
        elif start != arr[i+x][j+y]:
            return False
    return True

def check_right_diag (i, j):
    start = arr[i][j]
    for rd in right_diag :
        x, y = rd
        if not in_range(i+x, j+y):
            return False
        elif start != arr[i+x][j+y]:
            return False
    return True
                    


for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            if check_horiz or check_verti or check_left_diag or check_right_diag:
                if arr[i][j] == 1:
                    answer = [1, (i,j)]
                else:
                    answer = [2, (i, j)]
                break

if answer != 0:
    print(answer[0])
    print(answer[1][0], answer[1][1])
else:
    print(0)