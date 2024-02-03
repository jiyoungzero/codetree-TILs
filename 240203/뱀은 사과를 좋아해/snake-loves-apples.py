import sys
input = sys.stdin.readline 

n, m, K = map(int, input().split())
apple = [[False]*(n+1) for _ in range(n+1)]
snake = [(1,1)]
mapper = {
    'D':0,
    'U':1,
    'R':2,
    'L':3
}
answer = 0

def can_go(x, y):
    return 1 <= x < n+1 and 1<= y < n+1

def is_twisted(new_head):
    return new_head in snake

def push_front(new_head):
    #몸이 꼬이는 경우 -> False 리턴 
    if is_twisted(new_head):
        return False
    snake.insert(0, new_head)
    return True

def move_snake(nx, ny):
    if apple[nx][ny]:
        apple[nx][ny] = False
        if not push_front((nx, ny)):
            return False
    else:
        #꼬리빼기
        snake.pop()
        if not push_front((nx, ny)):
            return False
    return True

def move(move_dir, num):
    global answer
    dxs, dys = [1,-1,0,0],[0,0,1,-1]

    for _ in range(num):
        answer += 1
        x, y = snake[0]
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if not can_go(nx, ny):
            return False
        
        if not move_snake(nx, ny):
            return 

    return True

for _ in range(m):
    x, y = map(int, input().split())
    apple[x][y] = True

for _ in range(K): # K개의 명령을 수행
    move_dir, num = map(str, input().split())
    num = int(num)
    if not move(mapper[move_dir], num):
        break
print(answer)