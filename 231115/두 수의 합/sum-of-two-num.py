n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
numDict = {}

for i in range(n):
    if arr[i] in numDict.keys():
        numDict[arr[i]] += 1
    else: numDict[arr[i]] =1

setNum = list(set(arr))

for i in range(len(setNum)):
    if k-setNum[i] in numDict.keys():
        answer += ((numDict[setNum[i]])*numDict[k-setNum[i]])

print(answer//2)