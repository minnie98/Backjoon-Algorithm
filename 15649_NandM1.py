# N, M = map(int, input().split())
# visited = [False for i in range(N)]
# out = []
# #DFS 사용
# def N_M(depth, N, M):
#     if depth == M:
#         print(' '.join(map(str, out))) #출력
#         return
#     for i in range(N):
#         if not visited[i]: #방문하지 않은 노드에 대해서 탐색
#             visited[i] = True #방문 표시
#             out.append(i+1) #방문 내용
#             N_M(depth + 1, N, M) #재귀적으로
#             visited[i] = False #방문 완료
#             out.pop()
#
# N_M(0, N, M)
from itertools import permutations
N, M = map(int, input().split())

line = [x for x in range(1, N+1)]

for case in permutations(line,M):
    print(' '.join(map(str,case)))
