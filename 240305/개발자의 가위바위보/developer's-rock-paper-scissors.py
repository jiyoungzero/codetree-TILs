import sys
input =sys.stdin.readline


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
answer = []
win2lose = {'rock' : 'scissor', 'paper' : 'rock', 'scissor' : 'paper'} # 각각 무엇을 내면 이기는지

def count_win(dc):
    result = 0
    for a, b, in arr:
        if win2lose[dc[a]] == dc[b]:
            result += 1
    return result

tmp1 = {1:'rock', 2:"scissor", 3:'paper'}
tmp2 = {1: 'rock', 2 : 'paper', 3: 'scissor'}
tmp3 = {1: 'scissor',2 : "rock",3: "paper"}
tmp4 = {1: "scissor",2: "paper", 3 : "rock"}
tmp5 = { 1: "paper", 2: "scissor", 3: "rock"}
tmp6 ={ 1:"paper",2:"rock", 3: "scissor"}
answer.append(count_win(tmp1))
answer.append(count_win(tmp2))
answer.append(count_win(tmp3))
answer.append(count_win(tmp4))
answer.append(count_win(tmp5))
answer.append(count_win(tmp6))

print(max(answer))