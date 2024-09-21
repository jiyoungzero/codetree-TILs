n, k = map(int, input().split())
arr = list(map(int, input().split()))


max_sum = float('-inf')  # 초기 최대합을 매우 작은 값으로 설정

# 모든 연속 부분 수열을 고려하여 합을 계산
for start in range(n):
    current_sum = 0
    for end in range(start, n):
        current_sum += arr[end]
        if end - start + 1 >= k:  # 연속 부분 수열의 길이가 k 이상일 때
            max_sum = max(max_sum, current_sum)
print(max_sum)