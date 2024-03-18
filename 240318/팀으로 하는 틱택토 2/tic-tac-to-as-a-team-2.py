arr = [list(map(int, input())) for _ in range(3)]
win_set = []

# # 행
for i in range(3):
    tmp_set = set()
    for j in range(3):
        tmp_set.add(arr[i][j])
    if len(tmp_set) == 2 and tmp_set not in win_set:
        win_set.append(tmp_set)
# 열 
for j in range(3):
    tmp_set = set()
    for i in range(3):
        tmp_set.add(arr[i][j])
    if len(tmp_set) == 2 and tmp_set not in win_set:
        win_set.append(tmp_set)

# 대각선
if len(set([arr[0][2], arr[1][1], arr[2][0]])) == 2 and set([arr[0][2], arr[1][1], arr[2][0]]) not in win_set:
    win_set.append(set([arr[0][2], arr[1][1], arr[2][0]]))
if len(set([arr[0][0], arr[1][1], arr[2][2]])) == 2 and set([arr[0][0], arr[1][1], arr[2][2]]) not in win_set:
    win_set.append(set([arr[0][0], arr[1][1], arr[2][2]]))


# print(win_set)
print(len((win_set)))