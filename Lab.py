#############################
### Baekjoon Algorithm    ###
### No.14502              ###
#############################
# 1. 벽 세우기
# 2. 바이러스 퍼트리기
# 3. 안전구역 구하기

import sys
import copy

N, M = map(int, sys.stdin.readline().split())
Graph = []
for i in range(N):
    Line = list(map(int, sys.stdin.readline().split()))
    Graph.append(Line)

global maxArea
maxArea = 0
zero = []
virus = []

for i in range(N * M):
    row = i // M
    col = i % M

    if Graph[row][col] == 0:
        zero.append([row, col])
    elif Graph[row][col] == 2:
        virus.append([row, col])


def spreadVirus(G, row, col):
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    for direction in range(len(dx)):
        d_x = row + dx[direction]
        d_y = col + dy[direction]
        if (d_x >= 0 and d_x < N and d_y >= 0 and d_y < M):
            if G[d_x][d_y] == 0:
                G[d_x][d_y] = 2
                spreadVirus(G, d_x, d_y)

def safeArea(G):
    val = 0
    for i in range(N * M):
        row = i // M
        col = i % M
        if G[row][col] == 0:
            val += 1

    return val


def setWall(cnt, x):
    global maxArea
    if cnt == 0:
        G = copy.deepcopy(Graph)
        for i in range(len(virus)):
            spreadVirus(G, virus[i][0], virus[i][1])

        maxArea = max(maxArea, safeArea(G))
        return

    for i in range(x, len(zero)):
        Graph[zero[i][0]][zero[i][1]] = 1
        setWall(cnt - 1, i + 1)
        Graph[zero[i][0]][zero[i][1]] = 0

setWall(3, 0)
print(maxArea)
