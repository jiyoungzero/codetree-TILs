import sys
input = sys.stdin.readline
from collections import Counter, defaultdict 



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 행 
for i in range(n):
    for key, value in dict(Counter(arr[i])).items():
        if value == m:
            answer += 1
            break
# 열
for j in range(n):
    tmp_dict = defaultdict(int)
    for i in range(n):
        tmp_dict[arr[i][j]] += 1
    for key, value in tmp_dict.items():
        if value == m:
            answer += 1
            break
print(answer)