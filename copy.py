#객체의 3요소 value, type, id

# 불변객체 - int, float, bool, tuple, string, unicode
a = "asd"
b = a
a = "asdf"
print(a)    # asdf
print(b)    # asd

c = (10,2)
d = c
c = (10,3)
print(c)    # (10,3)
print(d)    # (10,2)

# 가변객체 - list, set, dict
# 단순복제 : 가변객체는 '='을 쓰면 같은 객체를 가리키기떄문에, 같은 주소를 쓴다
#           그래서 객체중 하나만 바꾸더라도 같은 객체를 가리키는것들을 바뀐값으로 출력한다.
# list
e = [1,2,3,["a","b"]]
f = e
e.append(4)
e[3].append("c")
print(e)    # [1,2,3,["a","b","c"],4]
print(f)    # [1,2,3,["a","b","c"],4]
# set
ab = {1,2,3}
af = ab
ab.remove(3)
print(ab)
print(af)
# dict
qw = {"1": "cksnd514"}
qe = qw
qw["1"] = "qwe21"
print(qw)   # {"1": "qwe21"}
print(qe)   # {"1": "qwe21"}

# shallow copy: 같은 객체를 가리키는것이 아니라 새로운 객체를 만들어주는것이다.
#               하지만 list속의 list와 같은 자식객체는 완전히 새로운 객체가 되지 않는다.
#               즉, list속 list는 바꾸면 따라서 바뀐다.
# list
import copy
e = [1,2,3,["a","b"]]
f = copy.copy(e)
e.append(5)
e[3].append("c")
print(e)    # [1, 2, 3, ['a', 'b', 'c'], 5]
print(f)    # [1, 2, 3, ['a', 'b', 'c']]

# deep copy: 객체 속의 자식객체까지 완전히 새로운 객체가 되도록 한다.
# list, 기타 객체에도 사용가능
from copy import deepcopy
e = [1,2,3,["a","b"]]
f = deepcopy(e)
e.append(5)
e[3].append("c")
print(e)    # [1, 2, 3, ['a', 'b', 'c'], 5]
print(f)    # [1, 2, 3, ['a', 'b']]

# set, dict은 그냥 b = copy(a) 하면 됨