import sys
input = sys.stdin.readline 
from collections import defaultdict

n, q = map(int, input().split())
nums = defaultdict(bool)
tmp = list(map(int, input().split()))
tmp.sort()
for ele in tmp:
    nums[ele] = True
prefix = [0]*(1000001)
for i in range(1, 1000001):
    if nums[i]:
        prefix[i] = prefix[i-1] + 1
    else:
        prefix[i] = prefix[i-1]
        
for _ in range(q):
    s, e = map(int, input().split())
    print(prefix[e]-prefix[s-1])