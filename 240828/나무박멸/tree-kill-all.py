import sys
input = sys.stdin.readline 

n = int(input())
#  단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
r_dxs, r_dys = [-1, -1, 1, 1], [-1, 1, -1, 1] 

dxs, dys = [0,0, 1, -1], [1, -1, 0, 0]