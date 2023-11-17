n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dic = dict()

for i in range(n):
    dic[arr[i]] = arr.count(arr[i])


for i in range(n):
    dic[arr[i]] -= 1
    for j in range(i):
        diff = k - (arr[i]+arr[j])
        if diff in dic:
            answer += dic[diff]

print(answer)