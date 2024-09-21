n, k = map(int, input().split())
arr = list(map(int, input().split()))
# DP 배열 초기화
dp = [0] * n

# 첫 번째 원소로 초기화
dp[0] = arr[0]
max_sum = dp[0]  # 최대 합 초기화

# DP 배열 계산
for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])  # 현재 원소를 포함하거나 새로 시작

    # 최대 합 업데이트
    max_sum = max(max_sum, dp[i])

# k개 이상의 수를 포함하는 최대 합 계산
current_sum = sum(arr[:k])  # 초기 k개 원소의 합
max_k_sum = current_sum  # k개 수의 최대 합

for i in range(k, n):
    current_sum += arr[i]  # 다음 원소 추가
    current_sum -= arr[i - k]  # k개 이상이므로 가장 오래된 원소 제거
    max_k_sum = max(max_k_sum, current_sum)  # 최대 k개 수의 합 업데이트
print(max_sum)