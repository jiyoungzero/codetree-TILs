import sys
input = sys.stdin.readline 

n, k, b = map(int, input().split())
blank = [int(input()) for _ in range(b)]

arr = [1 for i in range(1, n+1)]
arr = [0]+arr
for ele in blank:
    arr[ele] = 0
# print(arr)


# 가능한 최대의 연속 수 
# max_value = 0;
# for i in range(1, n+1):
#     max_value = max(max_value, )
p_prefix = [0]*(n+1)
nums = [i for i in range(n+1)]

for i in range(1, n+1):
    p_prefix[i] = p_prefix[i-1] + arr[i]
# print(*p_prefix)

prefix = [0]*(n-k+1)
for i in range(n-k+1):
    prefix[i] = p_prefix[i+k] - arr[i]

print(k - max(prefix))