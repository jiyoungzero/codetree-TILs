q = int(input())
n, m = 0, 0
stocks = [] # (id, w)
belts = {}
broken = set()

def establish_factory(cmd):
    global stocks, n, m
# 1. 공장 설립 : m개의 벨트, n개의 물건 (1개의 벨트 당 n/m개의 물건이 배치 됨.)
    n, m = cmd[0], cmd[1]
    for i in range(n):
        stocks.append((cmd[2+i], cmd[2+i+n]))
    
    stocks = stocks[::-1]

    for i in range(1, m+1):
        lst = []
        for j in range(n//m):
            lst.append(stocks.pop())
        belts[i] = lst 
    pass 

def off_under_wmax(w_max):
    global n, m
# 2. 물건 하차 : w_max를 넘으면 벨트 뒤로, 아니면 하차하기 
    off_sum = 0
    # print(w_max, belts)
    for i in range(1, m+1):
        if i in broken:continue
        nxt_lst = belts[i]
        if len(nxt_lst) == 0:continue
        idx, w = nxt_lst[0]
        if w <= w_max:
            off_sum += w 
            nxt_lst = nxt_lst[1:]
        else:
            nxt_lst = nxt_lst[1:]
            nxt_lst.append((idx, w))
        belts[i] = nxt_lst
    # print(belts)
    print(off_sum)

def remove_rid(r_id):
# 3. 물건 제거 : r_id 를 가진 물건을 하차 + r_id뒤에 있던 물건 한칸씩 앞으로, r_id가 없으면 -1출력 
    find = False
    for i in range(1, m+1):
        if i in broken:continue
        nxt_lst = belts[i]
        for j, (idx, w) in enumerate(belts[i]):
            if idx == r_id:
                find = True 
                nxt_lst = nxt_lst[:j] + nxt_lst[j+1:]
        belts[i] = nxt_lst
    # print("r_id 실행 후", belts) 
    print(r_id if find else -1)
                 

def check_fid(f_id):
# 4. 물건 확인 : f_id 가 존재하는 벨트 번호 출력 + 해당 상자 위에 있는 모든 상자 앞으로, 없으면 -1
    find = False

    for i in range(1, m+1):
        if i in broken:continue
        nxt_lst = belts[i]
        for j, (idx, w) in enumerate(belts[i]):
            if f_id == idx:
                find = True 
                print(i)
                nxt_lst = nxt_lst[j:] + nxt_lst[:j]
        belts[i] = nxt_lst 

    if not find:
        print(-1)

def break_belt(b_num):
    global broken
# 5. 벨트 고장 : b_num 출력 + b_num는 이제 사용 불가 
# + 오론쪽으로 검사하면서 최초의 정상 벨트에 b_num 위의 상자들 옮기기
# : 아래에서부터 순서대로 옮기기 
    # print(broken)
    if b_num in broken: 
        print(-1)
        return # 이미 망가져 있는 경우

    broken.add(b_num)   
    print(b_num)
    # 벨트가 3개
    # 고장 1번 
    # 1 + 1 = 2
    # 1 + 2 = 3
    # 1,2 3
    b_lst = belts[b_num]
    for plus in range(1, m+1):
        b_id = (b_num + plus)%m
        # print((b_num, plus, m+1), b_id)

        if b_id in broken:continue 
        else:
            nxt_lst = belts[b_id]
            nxt_lst += b_lst
            belts[b_id] = nxt_lst
            break 
    # print(belts)


for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 100: 
        establish_factory(cmd[1:])
    elif cmd[0] == 200:
        off_under_wmax(cmd[1])
    elif cmd[0] == 300:
        remove_rid(cmd[1])
    elif cmd[0] == 400:
        check_fid(cmd[1])
    else:
        break_belt(cmd[1])
    
 
    # print(cmd, "--> now belts : ", belts)
    # print()