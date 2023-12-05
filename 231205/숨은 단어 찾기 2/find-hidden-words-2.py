import sys
input =sys.stdin.readline

# 'LEE'의 개수

n,m = map(int, input().split())
arr = []

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

def in_range(x, y):
    return 0 <= x < n and 0<= y <m
for i in range(n):
    for j in range(m):
        for case in horiz:
    
            ni, nj = i+case