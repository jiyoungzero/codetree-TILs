import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

# 주어진 값들을 정렬합니다.
arr.sort()

# case1 : 3개의 숫자가 모두 연속한 경우
if arr[0]+ 1 == arr[1] and arr[1]+1 == arr[2]:
    answer = 0
# case2 : 양쪽의 두 개가 2 차이나는 경우
elif arr[0] + 2 == arr[1] or arr[1] + 2 == arr[2]:
    answer = 1
else: answer = 2
print(answer)