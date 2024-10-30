n = int(input())
arr = [ele for ele in range(1, n+1)]
start, end = 0,0
value = arr[start]

answer = 0


while start <= end and end < len(arr):
    if  value < n and end + 1 < len(arr):
        end += 1
        value += arr[end]
        
    else:
        if value == n:
            answer += 1
        value -= arr[start]
        start += 1

    
print(answer)