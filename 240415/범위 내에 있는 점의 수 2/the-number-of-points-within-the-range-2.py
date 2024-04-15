import sys
input = sys.stdin.readline 

n, q = map(int ,input().split())
dot_pos = list(map(int, input().split()))
MAX_N = 1000001
prefix = [0]*MAX_N
for i in dot_pos:
    prefix[i] = 1
for i in range(1, MAX_N):
    if prefix[i] == 1:
        prefix[i] = prefix[i-1]+1
    else:
        prefix[i] = prefix[i-1]

for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b]-prefix[a-1])