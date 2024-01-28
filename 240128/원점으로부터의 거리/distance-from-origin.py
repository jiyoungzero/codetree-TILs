import sys
input = sys.stdin.readline 

n = int(input())
info = []

def get_distance(x, y):
    return abs(x)+abs(y)

for i in range(1, n+1):
    x, y = map(int, input().split())
    dist = get_distance(x, y)
    info.append((i, dist))
info.sort(key=lambda x:(x[1], x[0]))

for ele in info:
    print(ele[0])