import sys
input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))
answer = sys.maxsize
arr.sort()


# -123 1 1 2 2  124
e = n-1
for s in range(n-1):
    tmp = arr[s] + arr[e]
    if s < e:
        answer = min(answer, abs(tmp))

    while True:
        if s >= e or (arr[s] + arr[e] < 0):break
        e -= 1
        answer = min(answer, abs(arr[s] + arr[e]))
print(answer)