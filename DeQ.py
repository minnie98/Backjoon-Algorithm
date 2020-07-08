#############################
### Baekjoon Algorithm    ###
### No.10866              ###
#############################

from sys import stdin
DEQ = []
N = int(stdin.readline())

for _ in range(N):
    line = stdin.readline().split()
    if line[0] == 'push_front': DEQ.insert(0,line[1])
    elif line[0] == 'push_back': DEQ.append(line[1])
    elif line[0] == 'front':
        if DEQ: print(DEQ[0])
        else: print(-1)
    elif line[0] == 'back':
        if DEQ: print(DEQ[-1])
        else: print(-1)
    elif line[0] == 'size': print(len(DEQ))
    elif line[0] == 'empty':
        if DEQ: print(0)
        else: print(1)
    elif line[0] == 'pop_front':
        if DEQ: print(DEQ.pop(0))
        else: print(-1)
    elif line[0] == 'pop_back':
        if DEQ: print(DEQ.pop(-1))
        else: print(-1)