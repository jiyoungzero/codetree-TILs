n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dic = dict()


for i in range(n-1):
    for j in range(i+1, n):
        ele = arr[i] + arr[j]

        diff = k-ele
        if diff in dic.keys():
            answer += dic[diff]
        
        if ele in dic.keys():
            dic[ele] += 1
        else:
            dic[ele] = 1
print(answer)