import sys
input = sys.stdin.readline 

n, q = map(int ,input().split())
dot_pos = list(map(int, input().split()))
MAX_N = 1000001
prefix = [0]*MAX_N
for i in dot_pos:
    prefix[i] = 1
# prefix = [0] + prefix

for i in range(MAX_N):
    if prefix[i] == 1:
        prefix[i] = prefix[i-1]+1
    else:
        prefix[i] = prefix[i-1]
prefix = [0] + prefix
for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b+1]-prefix[a])