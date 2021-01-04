n = int(input())    # 테스트케이스 개수

for i in range(n):
    array = list(input())
    r = int(array.pop(0))
    array.pop(0)
    for j in array:
        print(j*r,end='')
    print(" ")