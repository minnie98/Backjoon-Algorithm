#############################
### Backjoon Algorithm    ###    
### No.6603               ###
#############################


from itertools import combinations

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break

    for case in combinations(line[1:], 6):
        print(' '.join(map(str, case)))
    print('')
