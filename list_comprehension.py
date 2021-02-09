# [항목 for 항목 in 반복 가능한 객체]
a = [y for y in range(1,10)]

# [표현식 for 항목 in 반복 가능한 객체]
b = [i*2 for i in range(1,10)]

# [표현식 for 항목 in 반복 가능한 객체 if 조건문]
c = [i*3 for i in b if b%2 == 0]
