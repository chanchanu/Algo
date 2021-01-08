# 손익 분기점
cost1, cost2, price = map(int,input().split())
if((cost2 == price) or (cost2 > price)):
    print(-1)
else :
    i = cost1//(price - cost2) + 1
    print(i)
