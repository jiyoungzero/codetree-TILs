import sys
input = sys.stdin.readline


n = int(input())
arr = [0]*2002
answer = 0
start = 1000

for _ in range(n):
    x, cmd = map(str, input().split())
    if cmd == 'L':
        for i in range(start, start-int(x),-1):
            arr[i] += 1
    else:
        for i in range(start+1, start+int(x)+1):
            arr[i] += 1
    
    if cmd == 'R':
        start += int(x)
    else:
        start -= int(x)

for ele in arr:
    if ele > 1:
        answer += 1
print(answer)