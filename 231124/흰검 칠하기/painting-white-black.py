# 각 타일의 색이 바뀐 횟수 배열
# 각 타일의 색을 담은 배열 
import sys
input = sys.stdin.readline 

n = int(input())
arr = [[0,0,0] for _ in range(200002)] # [w,b, now_color]
start = 100000
w, b,g = 0,0,0

for _ in range(n):
    x, cmd = map(str, input().split())
    if cmd == 'L': # 흰색 = 0
        for i in range(start, start-int(x), -1):
            arr[i][0] += 1
            arr[i][2] = 'w'

        start -= (int(x)-1)

    else: # 검은색 = 1
        for i in range(start, start+int(x)):
            arr[i][1] += 1
            arr[i][2] = 'b'
        start += (int(x)-1)



for i in range(len(arr)):
    if arr[i][0] >=2 and arr[i][1] >= 2:
        g += 1
    else:
        if arr[i][2] == 'w':
            w += 1
        elif arr[i][2] == 'b':
            b += 1

print(w, b, g)