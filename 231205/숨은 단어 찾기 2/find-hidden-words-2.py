import sys
input =sys.stdin.readline

# 'LEE'의 개수

n,m = map(int, input().split())
arr = []
answer = 0

for _ in range(n):
    arr.append(input().rstrip())

# 평행 
horiz = [[(0, -2),(0, -1),(0,0)], [(0,-1), (0,0),(0,1)], [(0,0), (0,1),(0,2)]]
# 수직
verti = [[(-2, 0),(-1, 0),(0,0)], [(-1,0), (0,0),(1,0)], [(0,0), (1,0),(2,0)]]
# 오른쪽 대각선
r_diag = [[(-2,-2),(-1,-1),(0,0)], [(-1,-1), (0,0),(1,1)], [(0,0), (1,1),(2,2)]]
# 왼쪽 대각선
l_diag = [[(-2, 2),(-1,1),(0,0)], [(-1,1), (0,0),(1,-1)], [(0,0), (1,-1),(2,-2)]]
checked = []

def in_range(x, y):
    return 0 <= x < n and 0<= y <m

def search(lst):
    global checked
    global answer
    for jump in horiz:
        tmp = ''
        tmp_check = []
        for ji,jj in jump:
            ni, nj = i+ji, j+jj
            if in_range(ni, nj):
                tmp += arr[ni][nj]
                tmp_check.append([ni,nj])
            if len(tmp) == 3 and tmp_check not in checked and (tmp == 'LEE' or tmp == 'EEL'):
                answer += 1
                checked.append(tmp_check)
                print(tmp, tmp_check)

for i in range(n):
    for j in range(m):
        search(horiz)
        search(verti)
        search(r_diag)
        search(l_diag)

print(answer)