import sys
input = sys.stdin.readline

arr = input()
n = len(arr)
close = [0]*(n)
close[n-1] = 0

for i in range(n-1, 0, -1):
    if arr[i-2:i] == "))":
        close[i-1] = close[i] + 1
    else:
        close[i-1] = close[i]

answer =  0
for i in range(n-2):
    if arr[i:i+2] == "((":
        answer += close[i+2]

print(answer)