import sys
input =sys.stdin.readline 

n = int(input())
cmds = [input().split() for _ in range(n)]
w, b = 0, 0

offset = 1000001
arr = [0]*offset*2

cur = offset
for cmd in cmds:
    cnt, dir = int(cmd[0]), cmd[1]
    if dir == 'R':
        # print('R=', cur, cur+cnt)
        for i in range(cur, cur+cnt):
            arr[i] = 1 
        cur += (cnt-1)
    else:
        # print('L=', cur, cur-cnt)

        for i in range(cur, cur-cnt, -1):
            arr[i] = -1
            # print(i)
        cur -= (cnt-1)

print(arr.count(-1), arr.count(1))