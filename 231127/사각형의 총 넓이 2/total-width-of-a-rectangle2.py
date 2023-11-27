import sys
input =sys.stdin.readline


n = int(input())
arr = []
rect = [[0]*200 for _ in range(200)]
answer = 0

for _ in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    arr.append((x1+100,y1+100,x2+100,y2+100))



for ele in arr:
    x1, y1, x2, y2 = ele
    for i in range(x1, x2):
        for j in range(y1,y2):
            rect[i][j] = 1


for i in range(200):
    for j in range(200):
        if rect[i][j]:
            answer += 1
print(answer)