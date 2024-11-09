MOD = 10**9 + 7

def count_numbers(n):
    # dp[i][d]는 i자리 수에서 끝자리가 d인 경우의 수
    dp = [[0] * 10 for _ in range(n + 1)]
    
    # 1자리 수의 경우, 끝자리가 0~9는 모두 가능 (1개씩)
    for d in range(1, 10):
        dp[1][d] = 1
    
    # 2자리부터 n자리까지 계산
    for i in range(2, n + 1):
        for d in range(10):
            if d != 0:
                dp[i][d] += dp[i - 1][d - 1]  # 이전 자리가 d-1일 경우
            if d != 9:
                dp[i][d] += dp[i - 1][d + 1]  # 이전 자리가 d+1일 경우
            dp[i][d] %= MOD  # 모듈러 연산을 통해 10^9+7로 나눔
    
    # n자리 수에서 모든 끝자리를 고려한 결과를 합산
    result = sum(dp[n]) % MOD
    return result

# 입력 처리
n = int(input())
print(count_numbers(n))