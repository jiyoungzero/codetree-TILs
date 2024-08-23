n = int(input())
arr = [int(input()) for _ in range(n)]

prefix = [0]*(n+1)
prefix[1] = arr[0]
for i in range(2, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

answer = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        if (prefix[j] - prefix[i])%7 == 0:
            answer = max(answer, j-i)
print(answer)