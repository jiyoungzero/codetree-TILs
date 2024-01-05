import sys
input = sys.stdin.readline

n = int(input())
arr = [ input().rstrip() for _ in range(n)]
s_x, s_y = 0, 0
e_x, e_y = 0, 0
m = len(arr[0])
answer = int(1e9)
coins = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            s_x, s_y = i, j
        elif arr[i][j] == 'E':
            e_x, e_y = i, j
        elif arr[i][j].isdigit():
            coins.append((int(arr[i][j]),i, j))
        else:
            continue

coins.sort()
def choose_coins(depth, coin_cnt, path_len, x, y):
    global answer
    if coin_cnt==3:
        answer = min(answer, path_len+abs(x-e_x)+abs(y-e_y))
        return 

    if depth >= len(coins) or coin_cnt==3 or arr[x][y] == 'E':
        return 

    # 선택하는 경우
    if coin_cnt==0:
        val, nx, ny = coins[depth]
        choose_coins(depth+1, coin_cnt+1, path_len+abs(x-nx)+abs(y-ny), nx, ny)
    else:
        val, nx, ny = coins[depth]
        if val > int(arr[x][y]):
            choose_coins(depth+1, coin_cnt+1, path_len+abs(x-nx)+abs(y-ny), nx, ny)

    # 선택안하는 경우
    choose_coins(depth+1, coin_cnt, path_len, x, y)
        

choose_coins(0, 0, 0, s_x, s_y)
print(answer if answer < int(1e9) else -1)