from bisect import bisect_left

c, n = map(int, input().split())
red = [int(input()) for _ in range(c)]
black = [list(map(int, input().split())) for _ in range(n)]

red.sort()
black = sorted(black, key=lambda x: x[1])

ans = 0
visited = set()
for i in range(n):
    s, e = black[i]
    if s > red[-1]: continue
    if e < red[0]: continue

    s_idx, e_idx = bisect_left(red, s), bisect_left(red, e)

    if e_idx == len(red): e_idx -= 1
    if s_idx == len(red): s_idx -= 1

    # print(i, s_idx, e_idx)
    # while s_idx <= e_idx and red[s_idx] in visited:
    while s_idx < len(red) and red[s_idx] in visited and s_idx <= e_idx:
        s_idx += 1
    
    if s_idx > e_idx or red[s_idx] > e: # 못찾음
        continue
    else:
        # print(i, red[s_idx], visited)
        ans += 1
        visited.add(red[s_idx])

print(ans)