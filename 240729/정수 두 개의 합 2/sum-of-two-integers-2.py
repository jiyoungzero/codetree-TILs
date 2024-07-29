import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()


answer = 0
for i in range(n):
    j = i
    while j+1 < n and arr[i] + arr[j+1] <= k:
        answer += 1
        j += 1
        # print(i, j)
        
        
    
    # if j+1 < n and arr[i] + arr[j+1] <= k:
    #     answer += 1
    #     print(i, j+1)



print(answer)