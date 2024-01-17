import sys
input =sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
answer = -1
num_dict = defaultdict(list)

for idx, ele in enumerate(arr):
    num_dict[ele].append(idx+1)
set_arr = list(set(arr))
set_arr.sort()


if len(set_arr) == 1 or len(num_dict[set_arr[1]]) > 1:
    print(-1)
else:
    print(num_dict[set_arr[1]][0])