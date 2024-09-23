# 10 recompile

import re

data = '''
kim 840916-1094852
lee 921207-2059326
goo 981024-1674938
'''

pattern = re.compile('(\d{6})[-](\d{7})')
first = pattern.sub('\g<1>-*******',data)
print(first)
print(data)
#문자열 함수 for~~if~ data[시작위치]
#정규식 re.sub( '-[0-9]{4}-' , '-****-' , data)

second = re.sub('[0,9]{7}','*******',data)
print(second)





# 네번째
# phone = '010-1234-5678 이 찬혁'
# # 힌트 re.sub( '1패턴', "2변경적용", phone)
# model = re.sub( '-[0-9]{4}-' , '-****-', phone)
# print(phone)
# print(model)


# # 첫번째
# msg = 'my best blue my apple my cherry'
# info1 = re.findall('[a-zA-Z]{3,7}' ,msg)
# info2 = re.findall('[a-zA-Z0-9]{3,7}' ,msg)

# print(info1) # ['best', 'Flu', 'blue', 'cherry']
# print(info2) # ['best', '2400', 'Flu', 'blue', '357cher']



# #두번째
# msg = 'my best blue my apple my cherry'

# #어떤 단어가 몇번 나왔는지에 대해 찾기
# x = re.findall('my',msg)
# y = re.findall('blue',msg)
# z = re.findall('red',msg)
# print(x)
# print(y)
# print(z)

# 세번째
# msg = 'my best #@%! 24 newjeans 강해린 찬돌 blue my apple my cherry'

# ret1 = re.findall('[\w]+', msg)
# ret2 = re.findall('[\W]+', msg)                     #대문자만 나옴
# ret3 = re.findall('[a-zA-Z0-9가-힣]{3,10}', msg)    # {최소글자수, 최대글자수}
# ret4 = re.findall('[^a-zA-Z0-9가-힣]+', msg)        # ^x >> not x
# print('ret1:',ret1)
# print()
# print('ret2:',ret2)
# print()
# print('ret3:',ret3)
# print()
# print('ret4:',ret4)
