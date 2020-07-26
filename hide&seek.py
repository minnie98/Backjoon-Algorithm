#############################
### Baekjoon Algorithm    ###
### No.1697               ###
#############################

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dx = [-1, 1, 2]

Q = deque()

dst = [0] * 100001


def BFS(row):
    Q.append(row)
    while Q:
        X = Q.popleft()
        if X == K:
            return dst[X]

        for i in range(3):
            if i == 2:
                d_x = X * dx[i]
            else:
                d_x = X + dx[i]

            if 0 <= d_x < 100001 and dst[d_x] == 0:
                Q.append(d_x)
                dst[d_x] = dst[X] + 1

print(BFS(N))
