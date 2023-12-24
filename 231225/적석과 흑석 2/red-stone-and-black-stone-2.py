import sys
input = sys.stdin.readline
from sortedcontainers import SortedSet

c, n = map(int, input().split())
red_tmp = [int(input()) for _ in range(c)]
black_stones = []
for _ in range(n):
    a, b = tuple(map(int, input().split()))
    black_stones.append((b, a))
answer = 0

red_stones = SortedSet(red_tmp)

black_stones.sort()

for j in range(n):
    e, s = black_stones[j]
    t_idx = red_stones.bisect_left(s)
    if t_idx < len(red_stones) and red_stones[t_idx] <= e:
        answer += 1
        red_stones.remove(red_stones[t_idx])

print(answer)