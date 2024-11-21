n = int(input())  # 빙산의 개수
arr = [0] + [int(input()) for _ in range(n)] + [0] # 빙산 높이 리스트

# 이진 탐색의 범위 설정
left, right = 0, max(arr)
answer = 0
set_arr = sorted(set(arr[1:-1]), reverse = True)
heigth2idx = {value : idx for idx, value in enumerate(set_arr)}
visited = [False]*(n+2)

index_arr = [[] for _ in range(len(set_arr))]
for i in range(1, n+1):
    index_arr[heigth2idx[arr[i]]].append(i)

tmp = 0
for height in range(len(set_arr)):
    for idx in index_arr[height]:
        left, right = idx - 1, idx + 1
        if not visited[left] and not visited[right]:
            tmp += 1
        elif visited[left] and visited[right]:
            tmp -= 1

        visited[idx] = True
    answer = max(answer, tmp)


print(answer)
