#############################
### Baekjoon Algorithm    ###
### No.1012               ###
#############################

import sys
sys.setrecursionlimit(50000) #재귀제한높이 설정, 기본값(1000) 이상으로 설정 안하면 런타임 에러

T = int(input())
visit = []
Graph = []

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

Val = []


def DFS(row, col, M, N):
    visit[row][col] = True
    for i in range(4):
        d_x = dx[i] + row
        d_y = dy[i] + col
        if 0 <= d_x < M and 0 <= d_y < N:
            if not visit[d_x][d_y] and Graph[d_x][d_y] == 1:
                DFS(d_x, d_y, M, N)


for _ in range(T):
    cnt = 0
    M, N, K = map(int, sys.stdin.readline().split())
    Graph = [[0] * N for _ in range(M)]
    visit = [[False] * N for _ in range(M)]

    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        Graph[X][Y] = 1

    for i in range(M * N):
        row = i // N
        col = i % N
        if not visit[row][col] and Graph[row][col] == 1:
            DFS(row, col, M, N)
            cnt += 1

    Val.append(cnt)

for i in Val:
    print(i)
