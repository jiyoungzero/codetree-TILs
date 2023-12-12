n, k, t = map(str, input().split())
n, k = int(n), int(k)
arr = [input() for _ in range(n)]

target = []
for i in range(n):
    if arr[i].startswith(t):
        target.append(arr[i])
target.sort()
print(target[k-1])