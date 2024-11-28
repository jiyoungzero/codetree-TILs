n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0
if n == 1:
    print(0)
else:
    l, r = 0, 1
    while l < r and r < n:
        mn, mx = arr[l], arr[r]
        # mn >= mx*(0.9) : r += 1 
        # 아니면 l += 1
        if mn >= mx*(0.9):
            
            answer += 1
            r += 1
            if r == n and l < r-1:
                l += 1
                r = l + 1
        else:
            l += 1

    print(answer)