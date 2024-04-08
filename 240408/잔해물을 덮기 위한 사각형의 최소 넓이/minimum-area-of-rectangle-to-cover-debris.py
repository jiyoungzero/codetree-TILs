ax1, ay1, ax2, ay2 = map(int ,input().split())
bx1, by1, bx2, by2 = map(int, input().split())

OFFSET = 1000
arr = [[0]*2001 for _ in range(2001)]

for i in range(ax1+OFFSET, ax2+OFFSET):
    for j in range(ay1+OFFSET, ay2+OFFSET):
        arr[i][j] = 1

for i in range(bx1+OFFSET, bx2+OFFSET):
    for j in range(by1+OFFSET, by2+OFFSET):
        if arr[i][j] == 1:
            arr[i][j] = 0

min_x, min_y, max_x, max_y = 2001, 2001, -2001, -2001
for i in range(2001):
    for j in range(2001):
        if arr[i][j]:
            min_x = min(i, min_x)
            min_y = min(j, min_y)
            max_x = max(i, max_x)
            max_y = max(j, max_y)
# print(min_x, min_y, max_x, max_y)
if min_x == 2001 or min_y == 2001 or max_x == -2001 or max_y == -2001:
    print(0)
else:
    print((max_x-min_x+1)*(max_y-min_y+1))