n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0
one, two = 0, sum(arr)

while arr:
    one = arr.pop(0)
    two = arr.pop(-1)

    num_sum = one + two
    answer = max(answer, num_sum)

print(answer)