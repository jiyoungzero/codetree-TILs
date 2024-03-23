n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0

for i in range(n):
    tmp_cnt = 0
    tmp_sum = 0
    for j in range(i+1, n):
        if sum(arr[i:j])%7 == 0:
            tmp_cnt = (j-i)
            answer = max(answer, tmp_cnt)
print(answer)