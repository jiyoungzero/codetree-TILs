ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())

arr = [[0]*2001 for _ in range(2001)]
OFFSET = 1000
for i in range(ax1+OFFSET, ax2+OFFSET):
    for j in range(ay1+OFFSET, ay2+OFFSET):
        arr[i][j] = 1

for i in range(bx1+OFFSET, bx2+OFFSET):
    for j in range(by1+OFFSET, by2+OFFSET):
        arr[i][j] = 2
    
for i in range(mx1+OFFSET, mx2+OFFSET):
    for j in range(my1+OFFSET, my2+OFFSET):
        arr[i][j] = 3

answer = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1 or arr[i][j] == 2:
            answer += 1
print(answer)