#문자열 총합
n = int(input())    # 숫자 개수
array = list(input())   # 리스트로하여 각 문자마다 split되도록 만들기
array = [int(i) for i in array] # 각문자를 int로 변환
result = sum(array)             # list의 총합 
print(result)