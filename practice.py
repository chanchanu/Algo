a = input() # input()의 기본 자료형은 str이다
a = int(input()) # input()을 int자료형을 변환해서 저장
a = input().split() # 띄어쓰기 단위
a,b,c = map(int,input().split()) # 띄어쓰기 단위에서 int자료형으로 바꿔서 각 변수에 넣기
a = [int(i) for i in input().split()] # 띄어쓰기 단위에서 int 자료형으로 바꿔서 list로 저장 
# []는 list, ()는 튜플
# int(문자열,밑)
# ex int(11,2) = 3


# divmode(연산자,피연산자) -> 몫,나머지
# ex divmod(45,6) = (7,3)

# round(x, n)
# n음수 - x를 n만큼 반올림
# n양수 - x를 소수점 이하 n자리로 반올림
# ex round(1111,-2) -> 1100
# ex round(11.157,2) -> 11.16
num = int(input())
result = 0
for i in range(0,num):
    a = list(str(i))
    print(sum(int(a)))
    