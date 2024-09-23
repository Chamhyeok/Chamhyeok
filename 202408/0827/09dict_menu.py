# 09 dict_menu

import time
import sys

menu = dict()
flag = True
num, su, sel = 0, 0, 0
msg, info, message = 'NEWJEANS', 'HAERIN', 'KANG'

while flag:
    pass
    print()
    num = int(input('1. register 2. print 3. modify 4. delete 5. check 9. quit >> '))
    if num == 9 :
        print('QUIT')
        flag = False
        sys.exit()
    elif num == 1:
        key = input('메뉴 입력(KEY): >>>')
        price = input('가격 입력(VALUE): >>>')
        menu[key] = price
        print(key, '등록 완료')
        
    elif num == 2:
        for i,k in enumerate(menu):
            print(i+1, k, ' ', menu[k])

    elif num == 3:
        key = input('수정 대상 key값 입력: >>>')
        if menu.get(key) == None :
            print('입력하신 KEY값은 존재하지 않습니다.')
        else:
            menu[key] = price
            print(key, '수정 완료되었습니다.')

    elif num == 4:
        key = input('삭제 대상 키 값 입력 >>>')
        if menu.get(key) == None :
            print('입력하신 KEY값은 존재하지 않습니다.')
        else:
            menu.pop(key)
            print(key, '삭제 완료되었습니다.')

    elif num == 5:
        key = input('조회 대상 키 값 입력 >>>')
        if menu.get(key) == None :
            print('입력하신 KEY값은 존재하지 않습니다.')
        else:
            print(key, ':', price)
        




# my_site = dict()

# my_site[100] = 'NAVER'
# my_site[200] = 'KAKAO'
# my_site[300] = 'GOOGLE'

# for i,k in enumerate(my_site):      #index, key
#     print(i+1,k,' ', my_site[k])

# my_site[100] = 'ACORN'
# for k,v in my_site.items():         #key, value
#     print(k, ':', v)

# print(my_site[300])
# print(my_site.get(300))
# print(300 in my_site)