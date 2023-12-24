import sys
input = sys.stdin.readline
from sortedcontainers import SortedDict

c, n = map(int, input().split())
red_tmp = [int(input()) for _ in range(c)]
black_stones = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

red_stones = SortedDict()
for i in range(c):
    red_stones[red_tmp[i]] = False
# red_stones = dict(red_stones)
# print(red_stones)

for j in range(n):
    s, e = black_stones[j]

    for k, v in red_stones.items():
        if s <= k <= e and v == False:
            answer += 1
            red_stones[k] = True
            break


print(answer)