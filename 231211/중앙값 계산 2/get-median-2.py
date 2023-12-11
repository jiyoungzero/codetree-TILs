n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if (i+1)%2 == 1:
        tmp = arr[:i+1]
        tmp.sort()
        print(tmp[(i+1)//2], end=' ')