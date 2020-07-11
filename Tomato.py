#############################
### Baekjoon Algorithm    ###
### No.7576               ###
#############################

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
Graph = []

for _ in range(N):
    Line = list(map(int, sys.stdin.readline().split()))
    Graph.append(Line)

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

cnt = -1
Q = deque()

def BFS():
    global cnt
    while Q:
        cnt += 1
        for _ in range(len(Q)):
            X = Q.popleft()
            for i in range(4):
                d_x = dx[i] + X[0]
                d_y = dy[i] + X[1]

                if 0 <= d_x < N and 0 <= d_y < M:
                    if Graph[d_x][d_y] == 0:
                        Graph[d_x][d_y] = 1
                        Q.append([d_x, d_y])

for i in range(N * M):
    row = i // M
    col = i % M

    if Graph[row][col] == 1:
        Q.append([row,col])
BFS()

for i in range(N * M):
    if Graph[i // M][i % M] == 0:
        cnt = -1

print(cnt)
