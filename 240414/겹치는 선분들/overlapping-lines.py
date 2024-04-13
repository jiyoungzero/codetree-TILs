n, k = tuple(map(int, input().split()))
ans = 0

x = 0
segments = []
for _ in range(n):
    dist, c_dir = tuple(input().split())
    dist = int(dist)

    if c_dir == 'L':
        segments.append((x - dist, x))
        x -= dist
    else:
        segments.append((x, x + dist))
        x += dist

points = []
# 주어진 좌표의 범위가 큰 경우에는
# 각 선분을 두 지점으로 나눠서
# +1, -1로 담은 뒤,
# 정렬해줍니다.
for x1, x2 in segments:
    points.append((x1, +1)) # 시작점
    points.append((x2, -1)) # 끝점

# 정렬을 진행합니다.
points.sort()

# 각 위치에 적혀있는 숫자들의 합을 구하면
# 매 순간마다 겹치는 구간의 횟수가 구해집니다.
# 이 때 k 이상인 경우에 대해 구간의 합을 구하면 됩니다.
sum_val = 0
for i, (x, v) in enumerate(points):
    
    # k개 이상 겹치는 구간이라면
    # 해당 구간의 길이를 더해줍니다.
    if sum_val >= k:
        prev_x, _ = points[i-1]
        ans += (x-prev_x)

    # 적혀있는 가중치를 전부 더해줍니다.
    sum_val += v

print(ans)