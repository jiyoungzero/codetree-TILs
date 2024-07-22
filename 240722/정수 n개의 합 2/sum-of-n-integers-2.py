n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0]*n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]

answer = -int(1e9)
prefix = [0] + prefix
for i in range(k, n):
    answer = max(answer , prefix[i] - prefix[i-k])
print(answer)