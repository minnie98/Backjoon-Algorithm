#############################
### Backjoon Algorithm    ###
### No.10845              ###
#############################

from sys import stdin

Q = []

N = int(stdin.readline())

for _ in range(N):
    line = stdin.readline().split()
    if line[0] == 'push':
        Q.append(line[1])
    elif line[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(Q))
    elif line[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif line[0] == 'pop':
        if Q:
            print(Q.pop(0)) ##
        else:
            print(-1)
