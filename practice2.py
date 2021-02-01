x = list(input())
if(x[0] == '-'):
    x.pop(0)
    x.reverse()
    x.insert(0,'-')
else:
    x.reverse()
x = "".join(x)
result = int(x)
print(result)