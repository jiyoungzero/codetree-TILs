import sys
input = sys.stdin.readline
import heapq

t =int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    small, big = [], []
    middle = arr[0]
    answer = [middle]
    for i in range(1, n):
        if arr[i] < middle:
            heapq.heappush(small, -arr[i])
        else:
            heapq.heappush(big, arr[i])

        if i%2 == 0:
            # 중앙값 구하기
            if len(small) > len(big):
                tmp = -heapq.heappop(small)
                if middle > tmp:
                    heapq.heappush(big, middle)
                    middle = tmp
                else:
                    heapq.heappush(big, tmp)
            else:
                tmp = heapq.heappop(big)
                if middle < tmp:
                    heapq.heappush(small, -middle)
                    middle = tmp
                else:
                    heapq.heappush(small, -tmp)

            answer.append(middle)
    for ele in answer:
        print(ele, end = ' ')
    print()