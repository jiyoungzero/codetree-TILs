import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
bomb = [int(input()) for _ in range(n)]
answer = 0

bomb_pos = defaultdict(list)
for idx, val in enumerate(bomb):
    bomb_pos[val].append(idx)

for key, val in bomb_pos.items():
    
    for i in range(len(val)-1):
        if val[i]+k <= val[i+1]:
            answer = max(answer, key)
            break
print(answer)