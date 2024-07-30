import sys
input = sys.stdin.readline 

n = int(input())
k = int(input())
answer = sys.maxsize

l, r = 1, min(10**9, n**2)
while l <= r:
    mid = (l+r)//2
    cnt = 0
    cnt2 = 0
    for i in range(1, n+1):
        cnt += min(n, (mid//i))

    if cnt >= k:
        answer = min(answer, mid)
        r = mid - 1
    else:
        l = mid + 1
print(answer)