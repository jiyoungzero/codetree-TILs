from collections import defaultdict
import sys
input =sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
info = defaultdict(list)
visited = [False]*(n+1)
s_arr = arr[:]
s_arr.sort()

for i in range(n):
    info[s_arr[i]].append(i+1)

for idx, ele in enumerate(arr):
    for i in range(len(info[ele])):
        if not visited[info[ele][i]]:
            print(info[ele][i], end=" ")
            visited[info[ele][i]] = True
            break