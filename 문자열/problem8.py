#문자열 문제
dials_num = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
dials = input()
result = 0
for dial in dials:
    result += dials_num[ord(dial)-ord('A')]
print(result)