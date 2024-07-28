import sys
input = sys.stdin.readline 

n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr
answer = 100001

sum_v = 0
j = 0
for i in range(1, n+1):
    while j + 1 < n+1 and sum_v + arr[j+1] < s:
        sum_v += arr[j+1]
        j += 1

    if j+1 < n+1 and sum_v + arr[j+1] >= s:
        answer = min(answer ,j-i+2)
    # print(answer, "->", j-i+1, "j =", j, "i = ", i, sum_v)
    sum_v -= arr[i]

print(answer if answer < 100001 else -1)