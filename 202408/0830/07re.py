# 07 re

import re

msg = 'my best blue my apple my cherry'

#어떤 단어가 몇번 나왔는지에 대해 찾기
x = re.findall('my',msg)
y = re.findall('blue',msg)
z = re.findall('red',msg)
print(x)
print(y)
print(z)


msg = 'my best #@%! 24 newjeans 강해린 찬돌 blue my apple my cherry'

ret1 = re.findall( ' ', msg)
ret2 = re.findall( ' ', msg)
ret3 = re.findall( ' ', msg)
print(ret1)
print(ret2)
print(ret3)