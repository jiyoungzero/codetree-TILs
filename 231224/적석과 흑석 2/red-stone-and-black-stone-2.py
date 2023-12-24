import sys
input = sys.stdin.readline

c, n = map(int, input().split())
red_stones = [int(input()) for _ in range(c)]
black_stones = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

red_stones.sort()
black_stones.sort()
visited = [False]*len(black_stones)
for r in red_stones:
    for j, c in enumerate(black_stones):
        a, b = c
        if r < a or b < r:continue
        if a <= r <= b and not visited[j]:
            answer += 1
            visited[j] = True
            break

print(answer)