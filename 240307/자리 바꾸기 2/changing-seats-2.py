import sys
input = sys.stdin.readline 
from collections import defaultdict


n, k = map(int, input().split())
cmds = [list(map(int, input().split())) for _ in range(k)]
can_seat = defaultdict(set)
arr = [i for i in range(n)]

for i in range(n):
    can_seat[i].add(i)


for _ in range(3):
    for a, b in cmds:
        can_seat[arr[a-1]].add(b-1)
        can_seat[arr[b-1]].add(a-1)
        arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
        
for ele in can_seat.values():
    print(len(ele))