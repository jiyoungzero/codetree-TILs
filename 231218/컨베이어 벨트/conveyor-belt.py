import sys
input =sys.stdin.readline

n, t = map(int, input().split())
arr = []
for i in range(2):
    if i == 1:
        arr.append(list(map(int, input().split()))[::-1])
    else:
        arr.append(list(map(int, input().split())))


for _ in range(t):
    u_tmp = arr[0][-1] 
    d_tmp = arr[1][0]
    for i in range(n-2, -1,-1):
        arr[0][i+1] = arr[0][i]
    arr[0][0] = d_tmp

    for j in range(1, n):
        arr[1][j-1] = arr[1][j]
    arr[1][-1] = u_tmp

for i in range(2):
    if i == 1:
        for ele in arr[i][::-1]:
            print(ele, end=' ')
    else:
        for ele in arr[i]:
            print(ele, end=' ')
    print()