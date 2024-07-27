import sys
input = sys.stdin.readline 

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

l_dist = [0]*(n)
r_dist = [0]*(n)

def get_dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

for i in range(1, n):
    x1, y1 = arr[i-1]
    x2, y2 = arr[i]
    l_dist[i] = get_dist(x1, y1, x2, y2) + l_dist[i-1]

for i in range(n-2, -1, -1):
    x1, y1 = arr[i+1]
    x2, y2 = arr[i]
    r_dist[i] = get_dist(x1, y1, x2, y2) + r_dist[i+1]

answer = sys.maxsize
for skip in range(1, n-1):
    x1, y1 = arr[skip-1]
    x2, y2 = arr[skip+1]
    answer = min(answer, l_dist[skip-1]+r_dist[skip+1] + get_dist(x1, y1, x2, y2))
print(answer)