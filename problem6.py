# OX점수계산(증가)
n = int(input())    # testcase 개수
array = []

for i in range(n):
    score = 0
    scoresum = 0
    array = map(str,input().split())
    for j in array:
        if(j == 'O'):
            score += 1
        if(j == 'X'):
            score = 0
        scoresum = scoresum+score
    print(scoresum)