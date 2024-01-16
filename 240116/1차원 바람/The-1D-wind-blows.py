import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
direction = ['L', 'R']

commands = []
for _ in range(q):
    r, d = map(str, input().split())
    commands.append((int(r)-1, d))

def shift_arr(cur_dir, row):
    if cur_dir == 'L':
        arr[row].insert(0, arr[row].pop())
    else:
        arr[row].insert(m-1, arr[row].pop(0))


def have_same_number(cmd, row):
    if cmd == 'up' and row-1 >= 0:
        return any(
            arr[row-1][col] == arr[row][col]
            for col in range(m)
        )
    elif cmd == 'down' and row+1 < n:
        return any(
            arr[row+1][col] == arr[row][col]
            for col in range(m)
        )

    return False

def wind(cur_row, target_row, cur_dir):
    if target_row > cur_row:
        # 위로 전파
        shift_arr(direction[cur_dir], cur_row)

    else:
        # 아래로 전파
        shift_arr(direction[cur_dir], cur_row)

def print_arr(array):
    for row in array:
        print(*row)
    print()

for command in commands:
    r, d = command
    
    shift_arr(d, r) # 중심부 밀고
    up_flag = have_same_number('up',r) # 전파가능한지
    down_flag = have_same_number('down', r)
    up, down, cur_dir = r, r, direction.index(d)
    # 주변 전파
    while up_flag or down_flag:
        cur_dir = (cur_dir+1)%2
        if up_flag:
            up -= 1
            if up >= 0:
                wind(up, r, cur_dir)
                up_flag = have_same_number('up', up)
        if down_flag:
            down += 1
            if down < n:
                wind(down, r, cur_dir)
                down_flag = have_same_number('down',down)
                # print('now_down_row=', down, 'down_can_affect=', down_flag, 'dir=', direction[cur_dir])

print_arr(arr)