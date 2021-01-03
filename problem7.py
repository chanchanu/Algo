# 평균넘는 비율 구하기
n = int(input())    # 테스트케이스 개수
for i in range(n):
    array = input().split() # 인원,점수
    array = [int(j) for j in array] # int로 변환
    number = array.pop(0)           # 인원수는 따로 변수로 지정
    avg = sum(array)/len(array)     # 평균
    p = 0                           # 평균 넘는 인원수 구하는 변수
    for k in array:
        if k > avg:                 # 평균 넘을때 인원 ++
            p += 1
    result = p/number*100           # 평균 넘는 비율
    print(('%.3f' % result),end='') # 소수점 세째자리에서 반올림
    print('%')