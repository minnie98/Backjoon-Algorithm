#############################
### Baekjoon Algorithm    ###
### No.2667               ###
#############################
import sys

N = int(sys.stdin.readline())
Graph = []
visit = [[False] * N for _ in range(N)]

for i in range(N):
    Graph += sys.stdin.readline().split()

cnt = 1
Val = []

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


def Numbering(row, col):
    global cnt
    Q = [[row, col]]
    visit[row][col] = True
    while Q:
        X = Q.pop(0)
        for i in range(4):
            d_x = dx[i] + X[0]
            d_y = dy[i] + X[1]
            if 0 <= d_x < N and 0 <= d_y < N:
                if Graph[d_x][d_y] == '1' and not visit[d_x][d_y]:
                    Q.append([d_x, d_y])
                    visit[d_x][d_y] = True
                    Val[cnt - 1] += 1

for i in range(N * N):
    row = i // N
    col = i % N
    if not visit[row][col] and Graph[row][col] == '1':
        Val.append(1)
        Numbering(row, col)
        cnt += 1

Val.sort()
print(len(Val))
for i in Val:
    print(i)
