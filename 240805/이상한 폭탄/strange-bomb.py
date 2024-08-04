import sys
input = sys.stdin.readline 
from collections import defaultdict

n, k = map(int, input().split())
answer = -1
arr = [int(input()) for _ in range(n)]
nums = set(arr)
R = [0]*n # 오른쪽의 원소 중 가장 가까이에 잇으면서 동일한 수의 위치

num_dict = defaultdict(int)
for i in range(n):
    if arr[i] not in num_dict:
        num_dict[arr[i]] = i 
    else:
        if abs(num_dict[arr[i]] - i) <= k:
            answer = max(answer, arr[i])
print(answer if answer > 0 else '-1')