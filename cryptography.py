#############################
### Backjoon Algorithm    ###    
### No.1759               ###
#############################

from itertools import combinations

L,C = map(int, input().split())
alphabet = input().split()
alphabet.sort()

for case in combinations(alphabet, L):
    cnt = 0
    cnt2 = -2
    for x in case:
        if x in 'aeiou':
            cnt+=1
        else:
            cnt2+=1
    if cnt != 0 and cnt2>=0:
        print(''.join(map(str, case)))

