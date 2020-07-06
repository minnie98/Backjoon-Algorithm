#############################
### Backjoon Algorithm    ###
### No.1260               ###
#############################

from sys import stdin

N, M, V = map(int, stdin.readline().split())
Graph = [[0] * (N + 1) for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]

for _ in range(M):
    X, Y = map(int, stdin.readline().split())
    Graph[X][Y] = 1
    Graph[Y][X] = 1

def DFS(V):
    print(V, end=' ')
    visit[V] = 1
    for i in range(1, N + 1):
        if visit[i] == 0 and Graph[V][i] == 1:
            DFS(i)

def BFS(V):
    Q = [V]
    visit[V] = 0
    while (Q):
        V = Q[0]
        print(V, end=' ')
        Q.pop(0)
        for i in range(1, N + 1):
            if visit[i] == 1 and Graph[V][i] == 1:
                Q.append(i)
                visit[i] = 0

DFS(V)
print()
BFS(V)
