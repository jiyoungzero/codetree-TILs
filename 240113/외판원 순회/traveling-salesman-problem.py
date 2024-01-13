import sys
INT_MAX = sys.maxsize

n = int(input())
cost = [list(map(int, input().split()))for _ in range(n)]
visited = [False]*n
picked = []
answer = INT_MAX


def find_min(cnt):
    global answer
    # 모든 지점을 선택했을 시,
    # 최소 비용 계산
    if cnt == n:
        total_cost = 0
        for i in range(n-1):
            cur_cost = cost[picked[i]][picked[i+1]]
            if cur_cost == 0:
                return
            total_cost += cur_cost
        final_cost = cost[picked[-1]][0]
        if final_cost == 0:return

        total_cost += final_cost
        answer = min(answer, total_cost)
        return 


    # 방문할 지점 선택
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        picked.append(i)

        find_min(cnt+1)

        visited[i] = False
        picked.pop()
visited[0] = True
picked = [0]
find_min(1)
print(answer)