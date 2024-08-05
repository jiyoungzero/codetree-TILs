import sys
input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))
answer = sys.maxsize
arr = [0] + sorted(arr)

# -123 1 1 2 2  124
e = n
for s in range(1, n+1):
    if s < e:
        answer = min(answer, abs(arr[s] + arr[e]))

    while s < e - 1 and arr[s] + arr[e] > 0:
        e -= 1
        answer = min(answer, abs(arr[s] + arr[e]))
        
print(answer)