n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] + arr[j] == k:
            answer += 1

print(answer)