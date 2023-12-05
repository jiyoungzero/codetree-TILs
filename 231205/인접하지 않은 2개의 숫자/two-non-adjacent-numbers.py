import sys
input =sys.stdin.readline



n = int(input())
arr = list(map(int, input().split()))
answer = 0

for i in range(n):
    tmp = 0
    for j in range(i+2,n):
        tmp = arr[i] + arr[j]
        answer = max(answer, tmp)

    


print(answer)