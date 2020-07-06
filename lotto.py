from itertools import combinations

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break

    for case in combinations(line[1:], 6):
        print(' '.join(map(str, case)))
    print('')

#input().split() //값 여러개 받기 //결과는 문자열 리스트
#map //형 변환 (정수로, 실수로 , ... )