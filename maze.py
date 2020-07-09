#############################
### Baekjoon Algorithm    ###
### No.2178               ###
#############################

import sys

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze += list(sys.stdin.readline().split())

visit = [[False] * M for i in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
dst = [[0] * M for _ in range(N)]
dst[0][0] = 1


def Go(maze, row, col):
    visit[row][col] = True
    Q = [[row, col]]

    while Q:
        X = Q.pop(0)
        for i in range(4):
            d_x = dx[i] + X[0]
            d_y = dy[i] + X[1]
            if (d_x >= 0 and d_x < N and d_y >= 0 and d_y < M) and not visit[d_x][d_y]:
                if maze[d_x][d_y] == '1':
                    Q.append([d_x, d_y])
                    visit[d_x][d_y] = True
                    dst[d_x][d_y] = dst[X[0]][X[1]] + 1


Go(maze, 0, 0)
print(dst[N - 1][M - 1])
