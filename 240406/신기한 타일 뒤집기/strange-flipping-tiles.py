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
        for i in range(cur, cur+cnt):
            arr[i] = 1 
        cur += cnt
    else:
        for i in range(cur-cnt, cur):
            arr[i] = -1
        cur -= cnt

print(arr.count(-1), arr.count(1))