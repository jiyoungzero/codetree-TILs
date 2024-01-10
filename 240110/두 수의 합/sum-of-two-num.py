import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
num_info = defaultdict(int)
visited = dict()
answer = 0

for ele in arr:
    num_info[ele] += 1
    visited[ele] = False


for key, value in num_info.items():

    if (k-key) in num_info.keys() and not visited[k-key]:
        visited[k-key] = True
        visited[key] = True
        if key == (k-key):
            answer += (value*(value-1)//2)
            
        else:
            answer += (value*num_info[k-key])
        
print(answer)