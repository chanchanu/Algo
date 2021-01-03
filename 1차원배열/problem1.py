# 최대 최소 구하기

n = int(input())   # 입력개수
array = input().split()   # 입력되는 수
array = (map(int,array))
max = int(-999999)
min = int(999999)
for i in array:
    if i > max:
        max = i
    if i < min:
        min = i
print(min,max)
