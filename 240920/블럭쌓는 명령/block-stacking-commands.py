import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
cmds = [tuple(map(int, input().split())) for _ in range(k)]
arr = [0]*(n+1)
for s, e in cmds:
    for i in range(s, e+1):
        arr[i] += 1

arr = arr[1:]
arr.sort()
print(arr[n//2])