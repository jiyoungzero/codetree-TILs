import sys
input = sys.stdin.readline 
from collections import defaultdict

n, q = map(int, input().split())
nums =list(map(int, input().split()))

prefix = [0]*(1000001)
for num in nums:
    prefix[num] += 1

for i in range(1, 1000001):
    prefix[i] += prefix[i-1] 
        
for _ in range(q):
    s, e = map(int, input().split())
    if s == 0:
        print(prefix[e])
    else:
        print(prefix[e]-prefix[s-1])