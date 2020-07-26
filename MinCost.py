#############################
### Baekjoon Algorithm    ###
### No.1916               ###
#############################

import sys
import heapq

INF = sys.maxsize

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]

d = [INF] * (N + 1)
S = []

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].append([v, w])

src, dst = map(int, sys.stdin.readline().split())


def Dijkstra(src):
    d[src] = 0
    heapq.heappush(S, [0, src])

    while S:
        wei, vtx = heapq.heappop(S)

        for v, w in G[vtx]:
            v_weight = w + wei
            if v_weight < d[v]:
                d[v] = v_weight
                heapq.heappush(S, [v_weight, v])

Dijkstra(src)
print(d[dst])
