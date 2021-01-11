# 벌집 문제
n = int(input())

result = 1
b = 6
c = 1
i = 1

if n == 1:
    print(1)
    
else:
    while True:
        c = c + b #7,19,37,61.....
        result = result + 1  
        if n <= c: #경계값도 포함시키기 위해 등호 포함
            print(result)
            break #출력시켰으므로 탈출
        b += 6