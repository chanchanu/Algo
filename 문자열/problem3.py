#입력받은 문자열의 알파벳 존재 위치
s = input() # 입력받는 문자열
array = []

for i in range(26):
    array[i] = chr(97+i)

for i in range(len(array)):
    print(s.find(array[i]), end=' ')