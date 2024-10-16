def max_sum(n, arr):
    # DP 테이블 초기화
    dp = [[0] * n for _ in range(2)]

    # 첫 번째 열에 대한 초기화
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + arr[0][i])  # 위 행 선택
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + arr[1][i])  # 아래 행 선택

    return max(dp[0][n-1], dp[1][n-1])

# 입력 받기
n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]

# 최대 합 계산
result = max_sum(n, arr)

# 결과 출력
print(result)