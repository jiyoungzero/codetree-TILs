import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]
l, r = 1, sys.maxsize

answer = r
while l <= r:
    mid = (l+r)//2

    passed = 0
    for ele in arr:
        passed += (mid // ele)
    if passed >= n:
        r = mid - 1
        answer = min(answer, mid)
    else:
        l = mid + 1

print(answer)