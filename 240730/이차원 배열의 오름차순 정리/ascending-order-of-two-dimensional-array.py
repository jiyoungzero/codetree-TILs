import sys
input = sys.stdin.readline 

n = int(input())
k = int(input())
answer = sys.maxsize

l, r = 1, min(10**9, n**2)
while l <= r:
    mid = (l+r)//2
    cnt1 = 0
    cnt2 = 0
    for i in range(1, n+1):
        cnt1 += min(n, (mid//i))
        cnt2 += min(n, ((mid-1)//i))
    if cnt2 < k <= cnt1:
        # print(cnt2, cnt1, k, mid)
        answer = mid
        break
    elif cnt1 > k:
        r = mid - 1
    else:
        l = mid + 1
print(answer)