# 06 re

import re


# url = 'www.google.com'
# print(url)

# result = url.split('.')     #.을 기준으로 구분(자동으로 리스트화)

# conn = ';'
# print(conn.join(url))

msg = 'my best% 2400 Flu_it  is  blue%#357cherry'

info1 = re.findall('[a-zA-Z]{3,7}' ,msg)
info2 = re.findall('[a-zA-Z0-9]{3,7}' ,msg)

print(info1) # ['best', 'Flu', 'blue', 'cherry']
print(info2) # ['best', '2400', 'Flu', 'blue', '357cher']


my = re.findall('[a-zA-Z]{7,10}' ,msg)
if my:
    print(my)
else:
    print('[a-zA-Z]{7,10} 조건에 맞는 데이터가 없습니다.')
