import sys
input = sys.stdin.readline 

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
answer = int(1e9)

for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        segment = [0]*5
        for x, y in points:
            if x > i and y > j:
                segment[1] += 1
            elif x < i and y > j:
                segment[2] += 1
            elif x > i and y < j:
                segment[3] += 1
            else:
                segment[4] += 1
        min_val = max(segment)
        answer = min(answer, min_val)
print(answer)