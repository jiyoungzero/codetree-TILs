import sys
input = sys.stdin.readline 

# n = 개발자 수
# p = 처음 감염병에 걸린 개발자 번호
# k = 개인 당 감염을 일으킬 수 있는 악수의 수 (이후부터는 감염 X)
N, K, P, T = map(int, input().split())
handshake = []
answer = [0]*(N+1)
answer[P] = 1
have_cnt = [0]*(N+1)

for _ in range(T):
    t, x, y = map(int, input().split()) # t초에 x, y가 악수
    handshake.append((t, x, y))
handshake.sort()

for t, x, y in handshake:
    if answer[x] == 1 and answer[y] == 0:
        if have_cnt[x] < K:
            have_cnt[x] += 1
            answer[y] = 1
        else:
            continue
    elif answer[x] == 0 and answer[y] == 1:
        if have_cnt[y] < K:
            have_cnt[y] += 1
            answer[x] = 1
        else:
            continue
    elif answer[x] == 1 and answer[y] == 1:
        have_cnt[x] += 1
        have_cnt[y] += 1


# 출력
for ele in answer[1:]:
    print(ele, end='')