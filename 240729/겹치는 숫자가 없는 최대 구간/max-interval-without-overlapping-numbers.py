import sys
input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
max_len = 0
j = 0

counts = [0]*(max(arr)+1)

for i in range(1, n+1):
    while j+1 < n+1 and counts[arr[j+1]] + 1 < 2:
        counts[arr[j+1]] += 1
        j += 1
    
    max_len = max(max_len, j-i+1)
    counts[arr[i]] -= 1

print(max_len)