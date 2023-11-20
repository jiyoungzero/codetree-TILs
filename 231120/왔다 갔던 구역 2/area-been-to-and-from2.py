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
            start = i
    else:
        for i in range(start, start+int(x)):
            arr[i] += 1
            start = i

for ele in arr:
    if ele >= 2:
        answer += 1
print(answer)