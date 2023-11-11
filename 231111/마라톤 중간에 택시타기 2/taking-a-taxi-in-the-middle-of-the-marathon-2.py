n = int(input())
checkpt = [tuple(map(int, input().split())) for _ in range(n)]

answer = int(1e9)

def get_distance(arr):
    result = 0
    prevx, prevy = arr[0][0], arr[0][1]
    for i in range(1, n-1):
        result += (abs(prevx-arr[i][0])+ abs(prevy-arr[i][1]))
        prevx, prevy = arr[i][0], arr[i][1]
    return result

for i in range(1,n-1):
    copy_ckp = checkpt[:]
    del copy_ckp[i]
    answer = min(answer, get_distance(copy_ckp))

print(answer)