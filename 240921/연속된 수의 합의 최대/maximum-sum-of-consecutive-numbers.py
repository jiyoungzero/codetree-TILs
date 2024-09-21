n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [-int(1e9)] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

# k개 이상의 수를 선택해야 하므로, k-1번째까지의 합을 미리 계산
max_sum = sum(arr[:k])
current_sum = max_sum

for i in range(k, n):
    current_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, current_sum, current_sum + dp[i - k])

print(max_sum)