import sys
input = sys.stdin.readline 


n = int(input())
cmds = [tuple(map(int, input().split())) for _ in range(n)]
cmds.sort(key = lambda x : (x[0], -x[1]))
max_row = n
max_col = cmds[-1][1]
arr = [[0 ]* (max_col+1) for _ in range(max_row+1)]


final_row = 1
for cmd in cmds:
    s, e = cmd 
    cur_row = 0
    for i in range(max_row):
        flag = True
        cur_row = i
        for j in range(s, e+1):
            if arr[i][j] == 1:
                final_row += 1
                flag = False
                break
        if flag:
            for j in range(s, e+1):
                arr[cur_row][j] = 1
            break
print((max_col-2) * (final_row+1))