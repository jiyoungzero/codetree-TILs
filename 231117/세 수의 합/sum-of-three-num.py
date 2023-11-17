n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dic = dict()


for i in range(n):
    for j in range(i+1, n):
        ele = arr[i] + arr[j]

        diff = k-ele
        if diff in dic:
            answer += dic[diff]
        
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

print(answer)