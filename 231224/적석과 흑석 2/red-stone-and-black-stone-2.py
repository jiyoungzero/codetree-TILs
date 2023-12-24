import sys
input = sys.stdin.readline

c, n = map(int, input().split())
red_stones = [int(input()) for _ in range(c)]
black_stones = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

red_stones.sort()
black_stones.sort()
for r in red_stones:
    for c in black_stones:
        a, b = c
        if a <= r <= b:
            answer += 1
            black_stones.remove(c)

print(answer)