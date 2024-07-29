import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

j = n
answer = 0
for i in range(n):
    while j-1 >= i and arr[i] + arr[j-1] > k:
        j -= 1

        
    if j-1 >= i and arr[i] + arr[j-1] <= k:
        answer += (j-i-1)
        # print(i, j)
        # print(i, j+1)
print(answer)