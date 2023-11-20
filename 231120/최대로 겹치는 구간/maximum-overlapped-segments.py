# 구간은 start, end - 1 까지 표시.

import sys
input = sys.stdin.readline


n = int(input())
lines = [0]*200

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s+100, e+100):
        lines[i] += 1

print(max(lines))